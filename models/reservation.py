# -*- coding: utf-8 -*-
# from my_addons.sportclub.models import player
from odoo import models, fields, api
import uuid

from odoo.exceptions import ValidationError


class SportClubReservation(models.Model):
    _name = 'sportclub.reservation'
    _rec_name = 'code'

    code = fields.Char(compute='getuniqueid')
    duration = fields.Float(required=True)
    reservation_date = fields.Datetime('reservation date', default=fields.Datetime.today)
    player_id = fields.Many2one(comodel_name='sportclub.player',readonly=True )


    stadium_ids = fields.Many2many(comodel_name='sportclub.stadium', relation='class_reserv_stad',
                                     column1='code',
                                     column2='stadium_name' )


    def getuniqueid(self):
        self.code = uuid.uuid1()

    @api.constrains('duration')
    def _check_value(self):
        if self.duration <= 0:
            raise ValidationError('duration needs to be positive')



