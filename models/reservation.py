# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubReservation(models.Model):
    _name = 'sportclub.reservation'

    code = fields.Char()
    duration = fields.Float()
    reservation_date = fields.Datetime('reservation date')


