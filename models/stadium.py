# -*- coding: utf-8 -*-
import uuid

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SportClubStadium(models.Model):
    _name = 'sportclub.stadium'
    _rec_name = 'stadium_name'
    code_stadium = fields.Char(compute='getuniqueid')
    stadium_name = fields.Char(String='name', required=True)
    capacity = fields.Integer(required=True)
    creaation_date = fields.Datetime('creation date', required=True)
    sportclub_id = fields.Many2one(comodel_name='sportclub.sportclub' ,readonly=True)
  #  reservation_ids = fields.Many2one(comodel_name='sportclub.reservation',readonly=True)
    reservation_ids = fields.Many2many(comodel_name='sportclub.reservation', relation='class_reserv_stad',
                                   column1='stadium_name',
                                   column2='code' ,readonly=True)


    def getuniqueid(self):
        self.code_stadium = uuid.uuid1()

    @api.constrains('capacity')
    def _check_value(self):
        if self.capacity <= 0:
            raise ValidationError('capacity needs to be positive')



