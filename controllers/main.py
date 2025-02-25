# controllers/main.py Fichero main para manenejar las solicitudes http y la integracion con la API
from odoo import http
from odoo.http import request
from odoo.addons.modulo_CsFloat.models.csfloat_api import obtener_precio_skin


class CSFloatControllers(http.Controller):
    @http.route('/precio_skin', type='http', auth='public', website=True)
    def precio_skin(self, **kwargs):
        nombre_skin = kwargs.get('nombre_skin')
        if nombre_skin:
            try:
                datos = obtener_precio_skin(nombre_skin)
                if datos:
                    return request.render('modulo_CsFloat.template_precio_skin', {'datos': datos})
                else:
                    return request.render('modulo_CsFloat.template_skin_no_encontrada')
            except Exception as e:
                #Manejo de errores
                return request.render('modulo_CsFloat.template_error', {'error': str(e)})
        else: 
            return request.render('modulo_CsFloat.template_error', {'error': 'No se ha proporcionado correctamente el nombre de la skin'})
