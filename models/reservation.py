# -*- coding: utf-8 -*-
# from my_addons.sportclub.models import player
from odoo import models, fields
import uuid


class SportClubReservation(models.Model):
    _name = 'sportclub.reservation'
    _rec_name = 'code'
    # stadium_name = fields.Char(String='name')
    code = fields.Char(compute='getuniqueid')
    duration = fields.Float(required=True)
    reservation_date = fields.Datetime('reservation date', default=fields.Date.today)
    player_id = fields.Many2one(comodel_name='sportclub.player')
   #stadium_ids = fields.One2many(comodel_name='sportclub.stadium', inverse_name='reservation_ids')

    stadium_ids = fields.Many2many(comodel_name='sportclub.stadium', relation='class_reserv_stad',
                                     column1='code',
                                     column2='stadium_name')


    def getuniqueid(self):
        self.code = uuid.uuid1()



