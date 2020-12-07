# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubStadium(models.Model):
    _name = 'sportclub.stadium'

    code = fields.Char()
    capacity = fields.Integer()
    creaation_date = fields.Datetime('creation date')


