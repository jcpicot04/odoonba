# -*- coding: utf-8 -*-

from odoo import models, fields, api


class canso(models.Model):
    _name = 'musica.canso'
    _description = 'musica.canso'

    name = fields.Char(string="Titulo",required=True)
    artista = fields.Char(string="Artista")
    popularidad = fields.Integer(string="Popularidad")
    clients = fields.Many2many(comodel_name='res.partner',
                              relation='clients_cansons',
                              column2='client_id',
                              column1='canso_id')

    @api.model
    def restar_popularidad(self):
        cansons = self.env['musica.canso'].search([])
        for c in cansons:
            if(c.popularidad > 0):
                c.popularidad -=1

class client(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    name = fields.Char()
    cansons = fields.Many2many(comodel_name='musica.canso',
                              relation='clients_cansons',
                              column1='client_id',
                              column2='canso_id')

class canso_wizard(models.TransientModel):
    _name = 'musica.canso_wizard'

    cansons = fields.Many2one('musica.canso')


    @api.model
    def action_canso_wizard(self):
        action = self.env.ref('musica.action_canso_wizard').read()[0]
        return action

    def create_canso(self):

        client_id = self.env.context.get('user_id')
        client = self.env['res.partner'].browse([client_id])
        for c in self:
            client.write({'cansons':[(4,c.cansons.id,0)]})
            c.cansons.popularidad+=100
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'res_id': client.id,
            'view_mode': 'form',
            'target': 'current',
    	}