# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubReservation(models.Model):
    _name = 'sportclub.reservation'

    code = fields.Char()
    duration = fields.Float()
    reservation_date = fields.Datetime('reservation date')
    player_id = fields.Many2one(comodel_name='sportclub.player')
    stadium_ids = fields.One2many(comodel_name='sportclub.stadium', inverse_name='reservation_ids')


