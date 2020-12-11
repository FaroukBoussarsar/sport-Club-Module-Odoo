# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubStadium(models.Model):
    _name = 'sportclub.stadium'
    _rec_name = 'stadium_name'
    #code = fields.Char()
    stadium_name = fields.Char(String='name', required=True)
    capacity = fields.Integer(required=True)
    creaation_date = fields.Datetime('creation date', required=True)
    sportclub_id = fields.Many2one(comodel_name='sportclub.sportclub')
    reservation_ids = fields.Many2one(comodel_name='sportclub.reservation')
    stadium_ids = fields.Many2many(comodel_name='sportclub.reservation', relation='class_reserv_stad',
                                   column1='stadium_name',
                                   column2='code')



