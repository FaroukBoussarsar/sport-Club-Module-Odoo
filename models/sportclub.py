# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClub(models.Model):
    _name = 'sportclub.sportclub'
    sportclub_name = fields.Char(String='name')
    code = fields.Char()
    creaation_date = fields.Datetime('creation date')
    surface = fields.Float()
    owner_id = fields.Many2one(comodel_name='sportclub.owner')
