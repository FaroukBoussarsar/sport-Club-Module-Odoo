# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubPlayer(models.Model):
    _name = 'sportclub.player'

    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    birthday = fields.Date('Birthday')
    address = fields.Text('Address')
    email = fields.Char('email')
    phone = fields.Char('phone number')
    identity_card = fields.Char('Identity card')

    review_ids = fields.One2many(comodel_name='sportclub.review', inverse_name='player_id')
    reservation_ids = fields.One2many(comodel_name='sportclub.reservation', inverse_name='player_id')



