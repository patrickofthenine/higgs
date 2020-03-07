from django.db import models

class Higgs(models.Model):
    class_label = models.IntegerField(null=True)
    jet_1_btag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_1_eta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_1_phi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_1_pt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_2_btag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_2_eta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_2_phi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_2_pt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_3_btag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_3_eta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_3_phi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_3_pt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_4_btag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_4_eta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_4_phi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jet_4_pt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lepton_eta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lepton_pt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lepton_phi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_bb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_jj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_jjj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_jlv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_lv = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_wbb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_wwbb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    missing_energy_magnitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    missing_energy_phi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

class Meta:
    managed = False
    db_table = 'higgs'
