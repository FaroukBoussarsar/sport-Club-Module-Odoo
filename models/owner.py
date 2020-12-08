# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubOwner(models.Model):
    _name = 'sportclub.owner'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    birthday = fields.Date('Birthday')
    address = fields.Text('Address')
    email = fields.Char('email')
    phone = fields.Char('phone number')
    sportclub_ids = fields.One2many(comodel_name='sportclub.sportclub', inverse_name='owner_id')
