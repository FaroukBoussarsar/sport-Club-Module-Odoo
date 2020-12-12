# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from AptUrl.Helpers import _
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SportClubOwner(models.Model):
    _name = 'sportclub.owner'
    _rec_name = 'fullname'
    f_name = fields.Char('first name', required=True)
    l_name = fields.Char('last name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True)
    birthday = fields.Date('Birthday')
    address = fields.Text('Address')
    email = fields.Char('email', required=True)
    phone = fields.Char('phone number', required=True)
    sportclub_ids = fields.One2many(comodel_name='sportclub.sportclub', inverse_name='owner_id', required=True)
    fullname = fields.Char(compute='getfullname', default="owner")

    def getfullname(self):
        self.fullname = self.f_name + ' ' + self.l_name

    @api.constrains('email')
    def _check_value(self):
        regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not(re.search(regex, self.email)):
            raise ValidationError(_('invalid email !'))

