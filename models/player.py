# -*- coding: utf-8 -*-
import re

from AptUrl.Helpers import _

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


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
    image = fields.Image('player image', max_width=50, max_height=70, verify_resolution=False)
    review_ids = fields.One2many(comodel_name='sportclub.review', inverse_name='player_id')
    reservation_ids = fields.One2many(comodel_name='sportclub.reservation', inverse_name='player_id')
    fullname = fields.Char(compute='getfullname', default="player")

    def getfullname(self):
        self.fullname = self.f_name + ' ' + self.l_name

    @api.constrains('email')
    def _check_value(self):
        regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, self.email)):
            raise ValidationError(_('invalid email !'))

    @api.constrains('identity_card', 'phone')
    def _check_value(self):
        regex = '^[ 0-9]+$'
        if not (re.search(regex, self.phone)):
            raise ValidationError('invalid phone number ')
        if not(re.search(regex, self.identity_card)):
            raise ValidationError('invalid identity_card number')




