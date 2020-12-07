# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClub(models.Model):
    _name = 'sportclub.sportclub'
    name = fields.Char()
    code = fields.Char()
    creaation_date = fields.Datetime('creation date')
    surface = fields.Float()

