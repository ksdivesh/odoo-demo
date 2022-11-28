from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"  # odoo will create table hospital_patient in the db
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(
        comodel_name='hospital.patient', string="Patient")
    # related field is readonly by default
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    appointment_time = fields.Datetime(
        string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(
        string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
