# -*- coding: utf-8 -*-
from odoo import http

# class Universities(http.Controller):
#     @http.route('/universities/universities/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/universities/universities/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('universities.listing', {
#             'root': '/universities/universities',
#             'objects': http.request.env['universities.universities'].search([]),
#         })

#     @http.route('/universities/universities/objects/<model("universities.universities"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('universities.object', {
#             'object': obj
#         })