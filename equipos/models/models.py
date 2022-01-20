# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
from odoo.exceptions import ValidationError
from datetime import datetime
import random
import re
import base64

class equipos(models.Model):
    _name = 'equipos.equipos'
    _description = 'Equipos'

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'teams.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    name = fields.Char(string='Nombre', required=True, help='Nombre del equipo')
    conference = fields.Selection(selection=[('este', 'Este'),('oeste', 'Oeste')], string='Conferencia', default='este', required=True, help='Conferencia del equipo')
    budget = fields.Integer(string='Presupuesto',default=lambda s: random.randint(60000,90000),readonly=True)
    current_money = fields.Integer(string="Dinero restante",compute='_check_money',readonly=True)
    city = fields.Char(string='Ciudad', required=True, help='Ciudad del equipo')
    logo = fields.Image(default=_get_default_image, max_width=300, max_height=300)
    ligue = fields.Many2one('equipos.liga', ondelete='set null', help='Liga en la que juega')
    season = fields.Many2many('equipos.temporada',related='ligue.season')
    players = fields.One2many(string='Jugadores',comodel_name='equipos.jugadores',inverse_name='team')
    captain = fields.Many2one('equipos.jugadores',compute='_get_captain')
    victories = fields.Integer(string='Victorias',default=0,readonly=True)
    loses = fields.Integer(string='Derrotas',default=0,readonly=True)
    draws = fields.Integer(string='Empates',default=0,readonly=True)


    def _check_money(self):
        for team in self:
            team.current_money = team.budget
            for player in team.players:
                team.current_money -= float(player.pricepool)
    
    def _get_captain(self):
        for team in self:
            if team.players:
                team.captain = team.players[0].id
            else:
                team.captain = 0

    @api.onchange('ligue')
    def _reset_ligue(self):
        for l in self:
            print(l.ligue.finished)
            if l.ligue.finished == 'si':
                print('Permitido')
            elif l.ligue.finished:
                raise ValidationError('No puedes añadir un equipo a una liga que está en transcurso. Para poder realizar éste cambio la liga actual y a la que quieres cambiar deben indicarse como finalizadas.')

    @api.constrains('name','city')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            if regex.match(s.city):
                print(s.city)
            else:    
                raise ValidationError('La ciudad solo acepta letras. No introduzcas números o símbolos.')

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre del equipo no se puede repetir') ]

    def cambiar_budget(self):
        for s in self:
            budget = random.randint(50000,90000)
            for p in s.players:
                budget -= p.pricepool
                if budget > 0:
                    s.write({'budget':budget})
                else:
                    raise ValidationError('El presupuesto no ha sido cambiado debido a que sería inferior al precio de los jugadores.')


    @api.onchange('name')
    def _onchange_name(self):
        return { 'warning' : {'title':'Nombre','message':'Recuerda que el nombre de cada equipo debe ser único.','type':'notification'}}

class liga(models.Model):
    _name = 'equipos.liga'
    _description = 'Liga'

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'teams.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    name = fields.Char(string='Nombre')
    logo = fields.Image(default=_get_default_image, max_width=100, max_height=100)
    teams = fields.One2many(string='Equipos',comodel_name='equipos.equipos',inverse_name='ligue')
    top_teams = fields.One2many(string='Equipos con mayor budget',comodel_name='equipos.equipos',inverse_name='ligue',compute='_get_top_team')
    top_winners = fields.One2many(string='Tabla de clasificación', comodel_name='equipos.equipos',inverse_name='ligue',compute='_get_winners_team')
    finished = fields.Selection(selection=[('si', 'Si'),('no', 'No')],string='Liga terminada',default='no',required=True,readonly=True)
    matches = fields.Integer(string='Partidos jugados',default=0,readonly=True)
    calendar = fields.One2many(string='Partidos',comodel_name='equipos.partidos',inverse_name='ligue')
    season = fields.Many2many(comodel_name='equipos.temporada',
                              relation='league_season',
                              column1='league_id',
                              column2='season_id')

    def renovar_season(self):
            self.write({'season' : [(4,27,0)]})

    def reset_league(self):
        cont1 = 0
        cont2 = 0
        for p in self:
            for c in p.teams:
                cont1+=1
            cont2 = cont1 - 1
            cont3 = cont1 * cont2
            print(cont1)
            print(cont3)
            print(p.matches)
            if cont3 == p.matches:
                p.finished = 'si'
                p.matches = 0
                for t in p.teams:
                    t.victories = 0
                    t.loses = 0
                    t.draws = 0
                for i in p.calendar:
                    self.write({'calendar' : [(2,i.id,0)]})
            else:
                raise ValidationError('La temporada no ha terminado. Podrás volver a empezar cuando todos los partidos se hayan jugado (ida y vuelta)')


    def _get_top_team(self):
        for lig in self:
            if lig.teams:
                maxteam = lig.teams.filtered(lambda s: s.budget > 80000)
                lig.top_teams = maxteam.sorted(key=lambda s: s.budget, reverse=True)
            else:
                lig.top_teams = lig.teams

    def _get_winners_team(self):
        for lig in self:
            if lig.teams:
                maxteam = lig.teams.filtered(lambda s: s.victories > 0)
                lig.top_winners = maxteam.sorted(key=lambda s: s.victories, reverse=True)
            else:
                lig.top_winners = lig.teams
        
    @api.constrains('name')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')

    @api.constrains('season')
    def _check_season(self):
        for s in self:
            for p in s.season:
                if p.name == str(datetime.today().year):
                    print(p.name)
                else:    
                    raise ValidationError('Se debe jugar en la temporada ' + str(datetime.today().year))

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre de la liga no se puede repetir') ]

    @api.onchange('name')
    def _onchange_name(self):
        return { 'warning' : {'title':'Nombre','message':'Recuerda que el nombre de cada liga debe ser único.','type':'notification'}}

class temporada(models.Model):
    _name = 'equipos.temporada'
    _description = 'Temporada'

    name = fields.Char(string='Temporada')
    teamsseason = fields.Many2many(comodel_name='equipos.liga',
                                   relation='league_season',
                                   column2='league_id',
                                   column1='season_id',
                                   readonly=True)    
    def check_id(self):
        for l in self:
            print(l.id)
    
    @api.constrains('name')
    def _check_name(self):
        regex = re.compile('^(20[2-9]\d|2[1-9]\d{2}|[3-9]\d{3}|[1-9]\d{4,})$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('La temporada solo acepta a partir del año 2020 en el siguiente formato -> 2021')

    _sql_constraints = [ ('name_uniq','unique(name)','La temporada debe ser única') ]

class jugadores(models.Model):
    _name = 'equipos.jugadores'
    _description = 'Jugadores'

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'teams.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    name = fields.Char(string='Nombre',required=True)
    logo = fields.Image(default=_get_default_image, max_width=300, max_height=300)
    position = fields.Selection(selection=[('base', 'PG'),('escolta', 'SG'),('alero', 'SF'),('alapivot', 'PF'),('pivot', 'C')], string='Posicion', default='base', required=True, help='Posicion del jugador')
    nationality = fields.Char(string='Nacionalidad')
    team = fields.Many2one('equipos.equipos', ondelete='set null')
    free = fields.Selection(selection=[('si', 'Si'),('no', 'No')], string='Permitir su venta', default='no', required=True)
    pricepool = fields.Integer(default=lambda s: random.randint(2000,8000),readonly=True)

    @api.constrains('name','nationality')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            if regex.match(s.nationality):
                print(s.nationality)
            else:    
                raise ValidationError('La nacionalidad solo acepta letras. No introduzcas números o símbolos.')

    @api.constrains('team','pricepool','free')
    def _check_money(self):
        for s in self:
            if s.free == 'si' and (s.team.current_money - s.pricepool) > 0:
                print(s.team.budget - s.pricepool)
            else:    
                raise ValidationError('El equipo no dispone de dinero suficiente para realizar el fichaje o el jugador no está a la venta. Lo sentimos.')

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre completo del jugador no se puede repetir') ]            

class partidos(models.Model):
    _name = 'equipos.partidos'

    name = fields.Char(string='', compute='_get_name')
    date = fields.Datetime(string='Fecha',required=True)
    hours = fields.Integer(string='Duración del partido en horas',default=lambda s: random.randint(1,2),required=True,readonly=True)
    ligue = fields.Many2one('equipos.liga', required=True)
    team1 = fields.Many2one('equipos.equipos', string='Local',required=True)
    team2 = fields.Many2one('equipos.equipos', string='Visitante',required=True)
    team1_points = fields.Integer(string='Puntos local',default=lambda s: random.randint(80,120),readonly=True)
    team2_points = fields.Integer(string='Puntos visitante',default=lambda s: random.randint(80,120),readonly=True)
    result = fields.Char(string='Resultado',compute='_get_result',readonly=True)
    winner = fields.Char(string='Ganador',compute='_get_winner',readonly=True)

    def _get_result(self):
        for i in self:
            i.result = str(i.team1.name) + ' ' + str(i.team1_points) + " - " + str(i.team2.name) + ' ' + str(i.team2_points)

    def _get_name(self):
        for i in self:
            i.name = str(i.team1.name).upper() + " - " + str(i.team2.name).upper()
        
    def _get_winner(self):
        for i in self:
            if i.team1_points > i.team2_points:
                i.winner = i.team1.name
                i.team1.victories +=1
                i.team2.loses +=1
                i.ligue.matches +=1
            elif i.team2_points > i.team1_points:
                i.winner = i.team2.name
                i.team2.victories +=1
                i.team1.loses +=1
                i.ligue.matches +=1
            else:
                i.winner = 'Empate'
                i.team1.draws += 1
                i.team2.draws += 1
                i.ligue.matches +=1
        
    @api.constrains('name','ligue')
    def _get_matches(self):
        all_matches = self.env['equipos.partidos'].search([])
        all_match = all_matches[:-1]

        for p in all_match:
            for i in self:
                if str(p.name) == str(i.name) and str(i.ligue.name) == str(p.ligue.name):
                    raise ValidationError('Este partido ya ha sido jugado.')
                else:    
                    for p in i.ligue:
                        if p.finished == 'si':
                            p.finished = 'no'
            
    @api.constrains('team1','team2')
    def _check_teams(self):
        for s in self:
            if s.team1.name == s.team2.name:
                raise ValidationError('Los equipos deben ser distintos para poder jugar el partido.')
            else:    
                print('Movimiento correcto')

    @api.constrains('team1','team2','ligue')
    def _check_ligue(self):
        for s in self:
            if s.team1 not in s.ligue.teams:
                raise ValidationError(s.team1.name + ' no forma parte de la liga ' + s.ligue.name) 
            else:    
                print('Movimiento correcto')
            if s.team2 not in s.ligue.teams:
                raise ValidationError(s.team2.name + ' no forma parte de la liga ' + s.ligue.name) 
            else:    
                print('Movimiento correcto')