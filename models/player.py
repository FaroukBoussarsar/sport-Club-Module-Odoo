# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubPlayer(models.Model):
    _name = 'sportclub.player'
    _rec_name = 'fullname'
    f_name = fields.Char('first name', required=True)
    l_name = fields.Char('last name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True)
    birthday = fields.Date('Birthday')
    address = fields.Text('Address', required=True)
    email = fields.Char('email', required=True)
    phone = fields.Char('phone number', required=True)
    identity_card = fields.Char('Identity card', required=True)

    review_ids = fields.One2many(comodel_name='sportclub.review', inverse_name='player_id')
    reservation_ids = fields.One2many(comodel_name='sportclub.reservation', inverse_name='player_id')
    fullname = fields.Char(compute='getfullname', default="player")

    def getfullname(self):
        self.fullname = self.f_name + ' ' + self.l_name



