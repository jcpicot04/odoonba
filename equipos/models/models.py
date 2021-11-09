# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
from odoo.exceptions import ValidationError
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
    budget = fields.Integer(default=lambda s: random.randint(50000,90000),readonly=True)
    city = fields.Char(string='Ciudad', required=True, help='Ciudad del equipo')
    logo = fields.Image(default=_get_default_image, max_width=100, max_height=100)
    ligue = fields.Many2one('equipos.liga', ondelete='set null', help='Liga en la que juega')
    season = fields.Many2many('equipos.temporada',related='ligue.season')
    players = fields.One2many(string='Jugadores',comodel_name='equipos.jugadores',inverse_name='team')
    captain = fields.Many2one('equipos.jugadores',compute='_get_captain')

    
    def _get_captain(self):
        for team in self:
            if team.players:
                team.captain = team.players[0].id
            else:
                team.captain = 0

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
            s.write({'budget':budget})


class liga(models.Model):
    _name = 'equipos.liga'
    _description = 'Liga'

    name = fields.Char(string='Nombre')
    teams = fields.One2many(string='Equipos',comodel_name='equipos.equipos',inverse_name='ligue')
    season = fields.Many2many(comodel_name='equipos.temporada',
                              relation='league_season',
                              column1='league_id',
                              column2='season_id')

    @api.constrains('name')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre de la liga no se puede repetir') ]

class temporada(models.Model):
    _name = 'equipos.temporada'
    _description = 'Temporada'

    name = fields.Char(string='Temporada')
    teamsseason = fields.Many2many(comodel_name='equipos.liga',
                                   relation='league_season',
                                   column2='league_id',
                                   column1='season_id')

    @api.constrains('name')
    def _check_name(self):
        regex = re.compile('^(20[2-9]\d|2[1-9]\d{2}|[3-9]\d{3}|[1-9]\d{4,})$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('La temporada solo acepta a partir del año 2020 en el siguiente formato -> 2021')

class jugadores(models.Model):
    _name = 'equipos.jugadores'
    _description = 'Jugadores'

    name = fields.Char(string='Nombre',required=True)
    position = fields.Selection(selection=[('base', 'PG'),('escolta', 'SG'),('alero', 'SF'),('alapivot', 'PF'),('pivot', 'C')], string='Posicion', default='base', required=True, help='Posicion del jugador')
    nationality = fields.Char(string='Nacionalidad')
    team = fields.Many2one('equipos.equipos', ondelete='set null')

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

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre completo del jugador no se puede repetir') ]            