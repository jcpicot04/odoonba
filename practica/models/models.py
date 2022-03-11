# -*- coding: utf-8 -*-

from odoo import models, fields, api


class colegio(models.Model):
    _name = 'practica.colegio'
    _description = 'Colegio'

    name = fields.Char(string="Nombre",required=True)
    clases = fields.One2many(string='Clases',comodel_name='practica.clase',inverse_name='colegio')
    alumnos = fields.One2many(string='Alumnos',comodel_name='res.partner',inverse_name='colegio')
    profesores = fields.One2many(string='Profesores',comodel_name='practica.profesor',inverse_name='colegio')

class clase(models.Model):
    _name = 'practica.clase'
    _description = 'Clase'

    name = fields.Char(string="Nombre",required=True)
    colegio = fields.Many2one('practica.colegio',required=True)
    alumnos = fields.One2many(string='Alumnos',comodel_name='res.partner',inverse_name='clase')
    profesores = fields.Many2many(comodel_name='practica.profesor',
                              relation='profesores_clases',
                              column2='clase_id',
                              column1='profesor_id')

class alumno(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    name = fields.Char(string="Nombre",required=True)
    colegio = fields.Many2one('practica.colegio',compute="_get_colegio")
    clase = fields.Many2one('practica.clase',required=True)
    profesores = fields.Many2many('practica.profesor',related='clase.profesores',readonly=True)
    dias_cursados = fields.Integer(string="Dias cursados")
    is_alumno = fields.Boolean(string="Es alumno",compute="_get_es_alumno",store=True)

    @api.model
    def sumar_dias(self):
        alumnos = self.env['res.partner'].search([])
        for d in alumnos:
            if(d.is_alumno):
                d.dias_cursados +=1

    def _get_es_alumno(self):
        for a in self:
            if(a.clase):
                a.is_alumno = True
            else:
                a.is_alumno = False

    def reset_dias(self,records):
        for a in records:
            a.dias_cursados = 0

    @api.depends("clase")
    def _get_colegio(self):
        for c in self:
            c.colegio = c.clase.colegio

    def mostrar_mas_dias(self):
        todos_alumnos = self.env['res.partner'].search([]).filtered(lambda a: a.is_alumno)

        alumno_con_mas_dias = todos_alumnos.sorted(key=lambda a: a.dias_cursados, reverse=True)

        print(alumno_con_mas_dias[0].name)


class profesor(models.Model):
    _name = 'practica.profesor'
    _description = 'Profesor'

    name = fields.Char(string="Nombre",required=True)
    colegio = fields.Many2one('practica.colegio',required=True)
    clases = fields.Many2many(comodel_name='practica.clase',
                              relation='profesores_clases',
                              column1='clase_id',
                              column2='profesor_id')
    alumnos = fields.Many2many('res.partner',compute='_get_alumnos',readonly=True)

    def _get_alumnos(self):
        for c in self:
            for p in c.clases:
                c.alumnos+=p.alumnos

class alumno_wizard(models.TransientModel):
    _name = 'practica.alumno_wizard'

    name = fields.Char(string="Nombre",required=True)

    @api.model
    def action_alumno_wizard(self):
        action = self.env.ref('practica.action_alumno_wizard').read()[0]
        return action

    def create_alumno(self):
        clase = self.env.context.get('clase_id')
        for c in self:
            alumno_nuevo = c.env['res.partner'].create({'name': c.name,'clase':clase, 'is_alumno':True})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'res_id': alumno_nuevo.id,
            'view_mode': 'form',
            'view_id' : self.env.ref('practica.alumno_form').id,
            'target': 'current',
    	}


class colegio_wizard(models.TransientModel):
    _name = 'practica.colegio_wizard'

    state = fields.Selection([('1','Clase'),('2','Profesor'),('3','Alumno'),('4','Crear')],default='1')
    clase_name = fields.Char(string='Nombre clase')
    profesor_name = fields.Char(string="Nombre profesor")
    alumno_name = fields.Char(string="Nombre alumno")

    @api.model
    def action_colegio_wizard(self):
        action = self.env.ref('practica.action_colegio_wizard').read()[0]
        return action

    def next(self):
        if self.state == '1':
            self.state = '2'
        elif self.state == '2':
            self.state = '3'
        elif self.state == '3':
            self.state = '4'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
    
    def previous(self):
        if self.state == '2':
            self.state = '1'
        elif self.state == '3':
            self.state = '2'
        elif self.state == '4':
            self.state = '3'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def create_todo(self):
        for c in self:
            colegio = self.env.context.get('colegio_id')

            profesor = c.env['practica.profesor'].create({'name':c.profesor_name,'colegio':colegio})

            alumno = c.env['res.partner'].create({'name':c.alumno_name,'is_alumno':True})

            clase = c.env['practica.clase'].create({'name': c.clase_name,'colegio':colegio,'profesores':profesor,'alumnos': alumno})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'practica.clase',
            'res_id': clase.id,
            'view_mode': 'form',
            'target': 'current',
    	}

# class clase_wizard(models.TransientModel):

#     _name = 'preexamen.clase_wizard'

#     state = fields.Selection([('1','Clase'),('2','Profesor'),('3','Alumno')],default='1')
#     name = fields.Char()
#     c_name = fields.Char(string='Nombre Clase')
#     c_colegio = fields.Many2one('preexamen.colegio', required="True")
    
#     p_name = fields.Char(string='Nombre Profesor')
#     a_name = fields.Char(string='Nombre Alumno')


#     @api.model
#     def action_course_wizard(self):
#         action = self.env.ref('preexamen.action_clase_wizard').read()[0]
#         return action

#     def next(self):
#         if self.state == '1':
#             self.state = '2'
#         elif self.state == '2':
#             self.state = '3'
#         return {
#                 'type': 'ir.actions.act_window',
#                 'res_model': self._name,
#                 'res_id': self.id,
#                 'view_mode': 'form',
#                 'target': 'new',
#             }
#     def previous(self):
#         if self.state == '2':
#             self.state = '1'
#         elif self.state == '3':
#             self.state = '2'
#         elif self.state == '4':
#             self.state = '3'
#         return {
#             'type': 'ir.actions.act_window',
#             'res_model': self._name,
#             'res_id': self.id,
#             'view_mode': 'form',
#             'target': 'new',
#         }

#     def add_classroom(self):
#         for c in self:
#             c.write({'classrooms':[(0,0,{'name':c.c_name,'level':c.c_level})]})
#             return {
#                 'type': 'ir.actions.act_window',
#                 'res_model': self._name,
#                 'res_id': self.id,
#                 'view_mode': 'form',
#                 'target': 'new',
#             }