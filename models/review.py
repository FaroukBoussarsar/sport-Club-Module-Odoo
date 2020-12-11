# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubReview(models.Model):
    _name = 'sportclub.review'
    _rec_name = 'reviewer_name'
    code = fields.Char()
    score = fields.Float()
    description = fields.Text()
    creaation_date = fields.Datetime('creation date')
    sportclub_id = fields.Many2one(comodel_name='sportclub.sportclub')

    player_id = fields.Many2one(comodel_name='sportclub.player')

    reviewer_name = fields.Char(compute='get_reviewer_name')

    def get_reviewer_name(self):
        self.reviewer_name = self.player_id + ' review '

