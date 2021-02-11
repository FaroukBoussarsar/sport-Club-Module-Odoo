from odoo import models, fields
class UniversityDepartement(models.Model) :
    _name = 'university.departement'
    name = fields.Char()
    code = fields.Char()
