# -*- coding: utf-8 -*-
from odoo import models, fields, api
import uuid

from odoo.exceptions import ValidationError


class SportClubReview(models.Model):
    _name = 'sportclub.review'
    _rec_name = 'reviewer_name'
    code = fields.Char(compute='getuniqueid')
    score = fields.Float(required=True)
    description = fields.Text()
    creaation_date = fields.Datetime('creation date', default=fields.Datetime.today)
    sportclub_id = fields.Many2one(comodel_name='sportclub.sportclub' ,readonly=True,required=True)

    player_id = fields.Many2one(comodel_name='sportclub.player',readonly=True)

    reviewer_name = fields.Char(compute='get_reviewer_name', default="User")

    def get_reviewer_name(self):
        self.reviewer_name = str(self.player_id.fullname) + ' review '

    def getuniqueid(self):
        self.code = uuid.uuid1()

    @api.constrains('score')
    def _check_value(self):
        if not( 0 >= self.score > 10):
            raise ValidationError('score is between 0 and 10')
