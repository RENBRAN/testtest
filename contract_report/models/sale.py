# -*- coding: utf-8 -*-

from odoo import fields, models, api
import datetime
from datetime import timedelta
import pytz
from odoo.http import request
import pytz
from dateutil import tz


class Sale(models.Model):
    _inherit = 'sale.order'

  

    def contract_report(self):
        return self.env.ref('contract_report.actions_contracts_sale_order_new').report_action(self)

    def _compute_count_all(self):
        res = super(Sale, self)._compute_count_all()
        Odometer = self.env['sale.order']
        for record in self:
            record.odometer_count = Odometer.search_count([('vehicle_id', '=', record.id)])

        return res

    def _compute_date_start_new(self):
        zinfo_user = pytz.timezone(request.context.get('tz', 'utc') or 'utc') 
        user_tz = self.env.user.tz
        date_today = pytz.utc.localize(self.date_start).astimezone(zinfo_user)
        

        return date_today.time()

    def _compute_date_end_new(self):
        zinfo_user = pytz.timezone(request.context.get('tz', 'utc') or 'utc')  
        user_tz = self.env.user.tz
        date_new = pytz.utc.localize(self.date_end).astimezone(zinfo_user)
        return date_new.time()

    def _compute_time_start_new(self):
        zinfo_user = pytz.timezone(request.context.get('tz', 'utc') or 'utc') 
        user_tz = self.env.user.tz
        time_today = pytz.utc.localize(self.date_start).astimezone(zinfo_user)
        return time_today.date()
    
    def _compute_time_end_new(self):
        zinfo_user = pytz.timezone(request.context.get('tz', 'utc') or 'utc')  
        user_tz = self.env.user.tz
        time_end = pytz.utc.localize(self.date_end).astimezone(zinfo_user)
        return time_end.date()
   
        
    def _amount_total(self):
        add_amount = self.total_extra_price_with_taxes + self.amount_total
        return add_amount     

    def _add_remaining(self):
        add_amount = self.advance_payment + self.security_deposit
        remaining_amount = add_amount - self.amount_total 
        return remaining_amount  

    def _odometer_km(self):
        checkout = 0
        checkin = 0
        diff = 0
        for line in self.odometer_ids:
            if line.value:
                if checkin < line.value and checkin > 0:
                    checkout = checkin
                checkin = line.value
        diff = checkin - checkout
        return diff

    def _return_km(self):
        km = 0
        for line in self.odometer_ids:
            if line.value:
                km = line.value
        return km
