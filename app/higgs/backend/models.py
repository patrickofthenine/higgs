from django.db import models

class Higgs(models.Model):
    class_label = models.FloatField()
    jet_1_btag = models.FloatField()
    jet_1_eta = models.FloatField()
    jet_1_phi = models.FloatField()
    jet_1_pt = models.FloatField()
    jet_2_btag = models.FloatField()
    jet_2_eta = models.FloatField()
    jet_2_phi = models.FloatField()
    jet_2_pt = models.FloatField()
    jet_3_btag = models.FloatField()
    jet_3_eta = models.FloatField()
    jet_3_phi = models.FloatField()
    jet_3_pt = models.FloatField()
    jet_4_btag = models.FloatField()
    jet_4_eta = models.FloatField()
    jet_4_phi = models.FloatField()
    jet_4_pt = models.FloatField()
    lepton_eta = models.FloatField()
    lepton_pt = models.FloatField()
    lepton_phi = models.FloatField()
    m_bb = models.FloatField()
    m_jj = models.FloatField()
    m_jjj = models.FloatField()
    m_jlv = models.FloatField()
    m_lv = models.FloatField()
    m_wbb = models.FloatField()
    m_wwbb = models.FloatField()
    missing_energy_magnitude = models.FloatField()
    missing_energy_phi = models.FloatField()

class Meta:
    managed = False
    db_table = 'higgs'
