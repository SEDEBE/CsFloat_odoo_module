# controllers/main.py Fichero main para manenejar las solicitudes http y la integracion con la API
from odoo import http
from odoo.http import request
from odoo.addons.modulo_CsFloat.models.csfloat_api import obtener_precio_skin # type: ignore


class CSFloatControllers(http.Controller):
    @http.route('/precio_skin', type='http', auth='public', website=True)
    def precio_skin(self, **kwargs):
        nombre_skin = kwargs.get('nombre_skin')
        if nombre_skin: # type: ignore
            try:
                datos = obtener_precio_skin(nombre_skin)
                if datos:
                    return request.render('mi_modulo_csfloat.template_precio_skin',{'datos':datos})
                else:
                    return request.render('mi_modulo_csfloat.template_skin_no_encontrada')
            except Exception as e:
                #Manejo de errores
                return request.render('mi_modulo_csfloat.template_error', {'error': str(e)})
        else: 
            return request.render('mi_modulo_csfloat.template_error',{'error':'No se ha proporcionado correctamente el nombre de la skin'})
