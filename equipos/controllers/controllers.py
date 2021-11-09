# -*- coding: utf-8 -*-
# from odoo import http


# class Equipos(http.Controller):
#     @http.route('/equipos/equipos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/equipos/equipos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('equipos.listing', {
#             'root': '/equipos/equipos',
#             'objects': http.request.env['equipos.equipos'].search([]),
#         })

#     @http.route('/equipos/equipos/objects/<model("equipos.equipos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('equipos.object', {
#             'object': obj
#         })
