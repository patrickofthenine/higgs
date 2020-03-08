class Describe:
      fields = [
            # classification 
            'class_label', #0 background, 1 signal

            # props
            'jet_1_b-tag', #tag?
            'jet_1_eta', # -ln( tan(.5 * polar_angle) ) lol
            'jet_1_phi', # azimuthal angle
            'jet_1_pt',  # momentum
            'jet_2_b-tag', #
            'jet_2_eta',
            'jet_2_phi',
            'jet_2_pt',
            'jet_3_b-tag', 
            'jet_3_eta',
            'jet_3_phi',
            'jet_3_pt',
            'jet_4_b-tag',
            'jet_4_eta',
            'jet_4_phi',
            'jet_4_pt',
            'lepton_eta',
            'lepton_pT',
            'lepton_phi',
            'm_bb',
            'm_jj',

            # fns
            'm_jjj',
            'm_jlv',
            'm_lv',
            'm_wbb',
            'm_wwbb',
            'missing_energy_magnitude',
            'missing_energy_phi',
      ]

      def get_header_row(self):
            header = ''.join( str(field)+',' for field in self.fields)
            return header[:-1] #removes trailing ,

Describe().get_header_row()
