# Generated by Django 3.0.4 on 2020-03-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Higgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_label', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_1_btag', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_1_eta', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_1_phi', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_1_pt', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_2_btag', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_2_eta', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_2_phi', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_2_pt', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_3_btag', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_3_eta', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_3_phi', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_3_pt', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_4_btag', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_4_eta', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_4_phi', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('jet_4_pt', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('lepton_eta', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('lepton_pt', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('lepton_phi', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_bb', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_jj', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_jjj', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_jlv', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_lv', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_wbb', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('m_wwbb', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('missing_energy_magnitude', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('missing_energy_phi', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
            ],
        ),
    ]
