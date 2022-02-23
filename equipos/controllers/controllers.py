# -*- coding: utf-8 -*-
from odoo import http


class MyController(http.Controller):
   @http.route('/equipos/partido/', auth='user', type='json')
   def partido(self):
       return {
           'html': """
               <div id="equipos_banner">
                    <link href="/equipos/static/src/css/banner.css"
                       rel="stylesheet">
                   <h1>Partidos</h1>
                   <p>Creación de partidos:</p>
                   <a class="partido_button" type="action" data-reload-on-close="true" role="button" data-method="action_partido_wizard" data-model="equipos.partidos_wizard">
                   Crear partido
               </a>
               </div> """
       }

