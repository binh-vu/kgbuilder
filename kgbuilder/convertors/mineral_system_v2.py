from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_json(resource_0)
	
	writer_2 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "geokb": "https://geokb.wikibase.cloud/entity/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "xsd": "http://www.w3.org/2001/XMLSchema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "geo": "http://www.opengis.net/ont/geosparql#", "gkbi": "https://geokb.wikibase.cloud/entity/", "gkbp": "https://geokb.wikibase.cloud/wiki/Property/"})
	
	# Transform records of class mndr:EvidenceLayer:2
	pathway_potential_dataset_name_value_0_3 = resource_data_1["MineralSystem"]
	start_4 = 0
	end_5 = len(pathway_potential_dataset_name_value_0_3)
	for pathway_potential_dataset_name_index_1_6 in range(start_4, end_5):
		pathway_potential_dataset_name_value_1_7 = pathway_potential_dataset_name_value_0_3[pathway_potential_dataset_name_index_1_6]
		pathway_potential_dataset_name_value_2_8 = pathway_potential_dataset_name_value_1_7["pathway"]
		start_9 = 0
		end_10 = len(pathway_potential_dataset_name_value_2_8)
		for pathway_potential_dataset_name_index_3_11 in range(start_9, end_10):
			pathway_potential_dataset_name_value_3_12 = pathway_potential_dataset_name_value_2_8[pathway_potential_dataset_name_index_3_11]
			if not ("potential_dataset" in pathway_potential_dataset_name_value_3_12):
				continue
			else:
				pathway_potential_dataset_name_value_4_13 = pathway_potential_dataset_name_value_3_12["potential_dataset"]
				start_14 = 0
				end_15 = len(pathway_potential_dataset_name_value_4_13)
				for pathway_potential_dataset_name_index_5_16 in range(start_14, end_15):
					pathway_potential_dataset_name_value_5_17 = pathway_potential_dataset_name_value_4_13[pathway_potential_dataset_name_index_5_16]
					pathway_potential_dataset_name_value_6_18 = pathway_potential_dataset_name_value_5_17["name"]
					writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (26, pathway_potential_dataset_name_index_1_6, pathway_potential_dataset_name_index_3_11, pathway_potential_dataset_name_index_5_16), True, False)
					
					# Retrieve value of data property: pathway_potential_dataset_name
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/name", pathway_potential_dataset_name_value_6_18, None)
					
					# Retrieve value of data property: pathway_potential_dataset_score
					pathway_potential_dataset_score_value_0_19 = resource_data_1["MineralSystem"]
					pathway_potential_dataset_score_index_1_20 = pathway_potential_dataset_name_index_1_6
					pathway_potential_dataset_score_value_1_21 = pathway_potential_dataset_score_value_0_19[pathway_potential_dataset_score_index_1_20]
					pathway_potential_dataset_score_value_2_22 = pathway_potential_dataset_score_value_1_21["pathway"]
					pathway_potential_dataset_score_index_3_23 = pathway_potential_dataset_name_index_3_11
					pathway_potential_dataset_score_value_3_24 = pathway_potential_dataset_score_value_2_22[pathway_potential_dataset_score_index_3_23]
					if not ("potential_dataset" in pathway_potential_dataset_score_value_3_24):
						pass
					else:
						pathway_potential_dataset_score_value_4_25 = pathway_potential_dataset_score_value_3_24["potential_dataset"]
						pathway_potential_dataset_score_index_5_26 = pathway_potential_dataset_name_index_5_16
						pathway_potential_dataset_score_value_5_27 = pathway_potential_dataset_score_value_4_25[pathway_potential_dataset_score_index_5_26]
						pathway_potential_dataset_score_value_6_28 = pathway_potential_dataset_score_value_5_27["relevance_score"]
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", pathway_potential_dataset_score_value_6_28, None)
					
					writer_2.end_record()
	
	# Transform records of class mndr:Document:2
	pathway_id_document_value_0_29 = resource_data_1["MineralSystem"]
	start_30 = 0
	end_31 = len(pathway_id_document_value_0_29)
	for pathway_id_document_index_1_32 in range(start_30, end_31):
		pathway_id_document_value_1_33 = pathway_id_document_value_0_29[pathway_id_document_index_1_32]
		pathway_id_document_value_2_34 = pathway_id_document_value_1_33["pathway"]
		start_35 = 0
		end_36 = len(pathway_id_document_value_2_34)
		for pathway_id_document_index_3_37 in range(start_35, end_36):
			pathway_id_document_value_3_38 = pathway_id_document_value_2_34[pathway_id_document_index_3_37]
			if not ("supporting_references" in pathway_id_document_value_3_38):
				continue
			else:
				pathway_id_document_value_4_39 = pathway_id_document_value_3_38["supporting_references"]
				start_40 = 0
				end_41 = len(pathway_id_document_value_4_39)
				for pathway_id_document_index_5_42 in range(start_40, end_41):
					pathway_id_document_value_5_43 = pathway_id_document_value_4_39[pathway_id_document_index_5_42]
					if not ("document" in pathway_id_document_value_5_43):
						continue
					else:
						pathway_id_document_value_6_44 = pathway_id_document_value_5_43["document"]
						pathway_id_document_value_7_45 = pathway_id_document_value_6_44["id"]
						writer_2.begin_record("https://minmod.isi.edu/resource/Document", pathway_id_document_value_7_45, False, False)
						
						# Retrieve value of data property: pathway_id_document
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/id", pathway_id_document_value_7_45, None)
						
						# Retrieve value of data property: pathway_uri_document
						pathway_uri_document_value_0_46 = resource_data_1["MineralSystem"]
						pathway_uri_document_index_1_47 = pathway_id_document_index_1_32
						pathway_uri_document_value_1_48 = pathway_uri_document_value_0_46[pathway_uri_document_index_1_47]
						pathway_uri_document_value_2_49 = pathway_uri_document_value_1_48["pathway"]
						pathway_uri_document_index_3_50 = pathway_id_document_index_3_37
						pathway_uri_document_value_3_51 = pathway_uri_document_value_2_49[pathway_uri_document_index_3_50]
						if not ("supporting_references" in pathway_uri_document_value_3_51):
							pass
						else:
							pathway_uri_document_value_4_52 = pathway_uri_document_value_3_51["supporting_references"]
							pathway_uri_document_index_5_53 = pathway_id_document_index_5_42
							pathway_uri_document_value_5_54 = pathway_uri_document_value_4_52[pathway_uri_document_index_5_53]
							if not ("document" in pathway_uri_document_value_5_54):
								pass
							else:
								pathway_uri_document_value_6_55 = pathway_uri_document_value_5_54["document"]
								if not ("uri" in pathway_uri_document_value_6_55):
									pass
								else:
									pathway_uri_document_value_7_56 = pathway_uri_document_value_6_55["uri"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/uri", pathway_uri_document_value_7_56, None)
						
						# Retrieve value of data property: pathway_doi
						pathway_doi_value_0_57 = resource_data_1["MineralSystem"]
						pathway_doi_index_1_58 = pathway_id_document_index_1_32
						pathway_doi_value_1_59 = pathway_doi_value_0_57[pathway_doi_index_1_58]
						pathway_doi_value_2_60 = pathway_doi_value_1_59["pathway"]
						pathway_doi_index_3_61 = pathway_id_document_index_3_37
						pathway_doi_value_3_62 = pathway_doi_value_2_60[pathway_doi_index_3_61]
						if not ("supporting_references" in pathway_doi_value_3_62):
							pass
						else:
							pathway_doi_value_4_63 = pathway_doi_value_3_62["supporting_references"]
							pathway_doi_index_5_64 = pathway_id_document_index_5_42
							pathway_doi_value_5_65 = pathway_doi_value_4_63[pathway_doi_index_5_64]
							if not ("document" in pathway_doi_value_5_65):
								pass
							else:
								pathway_doi_value_6_66 = pathway_doi_value_5_65["document"]
								if not ("doi" in pathway_doi_value_6_66):
									pass
								else:
									pathway_doi_value_7_67 = pathway_doi_value_6_66["doi"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/doi", pathway_doi_value_7_67, None)
						
						# Retrieve value of data property: pathway_journal
						pathway_journal_value_0_68 = resource_data_1["MineralSystem"]
						pathway_journal_index_1_69 = pathway_id_document_index_1_32
						pathway_journal_value_1_70 = pathway_journal_value_0_68[pathway_journal_index_1_69]
						pathway_journal_value_2_71 = pathway_journal_value_1_70["pathway"]
						pathway_journal_index_3_72 = pathway_id_document_index_3_37
						pathway_journal_value_3_73 = pathway_journal_value_2_71[pathway_journal_index_3_72]
						if not ("supporting_references" in pathway_journal_value_3_73):
							pass
						else:
							pathway_journal_value_4_74 = pathway_journal_value_3_73["supporting_references"]
							pathway_journal_index_5_75 = pathway_id_document_index_5_42
							pathway_journal_value_5_76 = pathway_journal_value_4_74[pathway_journal_index_5_75]
							if not ("document" in pathway_journal_value_5_76):
								pass
							else:
								pathway_journal_value_6_77 = pathway_journal_value_5_76["document"]
								if not ("journal" in pathway_journal_value_6_77):
									pass
								else:
									pathway_journal_value_7_78 = pathway_journal_value_6_77["journal"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/journal", pathway_journal_value_7_78, None)
						
						# Retrieve value of data property: pathway_authors
						pathway_authors_value_0_79 = resource_data_1["MineralSystem"]
						pathway_authors_index_1_80 = pathway_id_document_index_1_32
						pathway_authors_value_1_81 = pathway_authors_value_0_79[pathway_authors_index_1_80]
						pathway_authors_value_2_82 = pathway_authors_value_1_81["pathway"]
						pathway_authors_index_3_83 = pathway_id_document_index_3_37
						pathway_authors_value_3_84 = pathway_authors_value_2_82[pathway_authors_index_3_83]
						if not ("supporting_references" in pathway_authors_value_3_84):
							pass
						else:
							pathway_authors_value_4_85 = pathway_authors_value_3_84["supporting_references"]
							pathway_authors_index_5_86 = pathway_id_document_index_5_42
							pathway_authors_value_5_87 = pathway_authors_value_4_85[pathway_authors_index_5_86]
							if not ("document" in pathway_authors_value_5_87):
								pass
							else:
								pathway_authors_value_6_88 = pathway_authors_value_5_87["document"]
								if not ("authors" in pathway_authors_value_6_88):
									pass
								else:
									pathway_authors_value_7_89 = pathway_authors_value_6_88["authors"]
									start_90 = 0
									end_91 = len(pathway_authors_value_7_89)
									for pathway_authors_index_8_92 in range(start_90, end_91):
										pathway_authors_value_8_93 = pathway_authors_value_7_89[pathway_authors_index_8_92]
										if True:
											writer_2.write_data_property("https://minmod.isi.edu/resource/authors", pathway_authors_value_8_93, None)
						
						# Retrieve value of data property: pathway_description_document
						pathway_description_document_value_0_94 = resource_data_1["MineralSystem"]
						pathway_description_document_index_1_95 = pathway_id_document_index_1_32
						pathway_description_document_value_1_96 = pathway_description_document_value_0_94[pathway_description_document_index_1_95]
						pathway_description_document_value_2_97 = pathway_description_document_value_1_96["pathway"]
						pathway_description_document_index_3_98 = pathway_id_document_index_3_37
						pathway_description_document_value_3_99 = pathway_description_document_value_2_97[pathway_description_document_index_3_98]
						if not ("supporting_references" in pathway_description_document_value_3_99):
							pass
						else:
							pathway_description_document_value_4_100 = pathway_description_document_value_3_99["supporting_references"]
							pathway_description_document_index_5_101 = pathway_id_document_index_5_42
							pathway_description_document_value_5_102 = pathway_description_document_value_4_100[pathway_description_document_index_5_101]
							if not ("document" in pathway_description_document_value_5_102):
								pass
							else:
								pathway_description_document_value_6_103 = pathway_description_document_value_5_102["document"]
								if not ("description" in pathway_description_document_value_6_103):
									pass
								else:
									pathway_description_document_value_7_104 = pathway_description_document_value_6_103["description"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/description", pathway_description_document_value_7_104, None)
						
						# Retrieve value of data property: pathway_title_document
						pathway_title_document_value_0_105 = resource_data_1["MineralSystem"]
						pathway_title_document_index_1_106 = pathway_id_document_index_1_32
						pathway_title_document_value_1_107 = pathway_title_document_value_0_105[pathway_title_document_index_1_106]
						pathway_title_document_value_2_108 = pathway_title_document_value_1_107["pathway"]
						pathway_title_document_index_3_109 = pathway_id_document_index_3_37
						pathway_title_document_value_3_110 = pathway_title_document_value_2_108[pathway_title_document_index_3_109]
						if not ("supporting_references" in pathway_title_document_value_3_110):
							pass
						else:
							pathway_title_document_value_4_111 = pathway_title_document_value_3_110["supporting_references"]
							pathway_title_document_index_5_112 = pathway_id_document_index_5_42
							pathway_title_document_value_5_113 = pathway_title_document_value_4_111[pathway_title_document_index_5_112]
							if not ("document" in pathway_title_document_value_5_113):
								pass
							else:
								pathway_title_document_value_6_114 = pathway_title_document_value_5_113["document"]
								if not ("title" in pathway_title_document_value_6_114):
									pass
								else:
									pathway_title_document_value_7_115 = pathway_title_document_value_6_114["title"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/title", pathway_title_document_value_7_115, None)
						
						# Retrieve value of data property: pathway_volume
						pathway_volume_value_0_116 = resource_data_1["MineralSystem"]
						pathway_volume_index_1_117 = pathway_id_document_index_1_32
						pathway_volume_value_1_118 = pathway_volume_value_0_116[pathway_volume_index_1_117]
						pathway_volume_value_2_119 = pathway_volume_value_1_118["pathway"]
						pathway_volume_index_3_120 = pathway_id_document_index_3_37
						pathway_volume_value_3_121 = pathway_volume_value_2_119[pathway_volume_index_3_120]
						if not ("supporting_references" in pathway_volume_value_3_121):
							pass
						else:
							pathway_volume_value_4_122 = pathway_volume_value_3_121["supporting_references"]
							pathway_volume_index_5_123 = pathway_id_document_index_5_42
							pathway_volume_value_5_124 = pathway_volume_value_4_122[pathway_volume_index_5_123]
							if not ("document" in pathway_volume_value_5_124):
								pass
							else:
								pathway_volume_value_6_125 = pathway_volume_value_5_124["document"]
								if not ("volume" in pathway_volume_value_6_125):
									pass
								else:
									pathway_volume_value_7_126 = pathway_volume_value_6_125["volume"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/volume", pathway_volume_value_7_126, None)
						
						# Retrieve value of data property: pathway_issue_document
						pathway_issue_document_value_0_127 = resource_data_1["MineralSystem"]
						pathway_issue_document_index_1_128 = pathway_id_document_index_1_32
						pathway_issue_document_value_1_129 = pathway_issue_document_value_0_127[pathway_issue_document_index_1_128]
						pathway_issue_document_value_2_130 = pathway_issue_document_value_1_129["pathway"]
						pathway_issue_document_index_3_131 = pathway_id_document_index_3_37
						pathway_issue_document_value_3_132 = pathway_issue_document_value_2_130[pathway_issue_document_index_3_131]
						if not ("supporting_references" in pathway_issue_document_value_3_132):
							pass
						else:
							pathway_issue_document_value_4_133 = pathway_issue_document_value_3_132["supporting_references"]
							pathway_issue_document_index_5_134 = pathway_id_document_index_5_42
							pathway_issue_document_value_5_135 = pathway_issue_document_value_4_133[pathway_issue_document_index_5_134]
							if not ("document" in pathway_issue_document_value_5_135):
								pass
							else:
								pathway_issue_document_value_6_136 = pathway_issue_document_value_5_135["document"]
								if not ("issue" in pathway_issue_document_value_6_136):
									pass
								else:
									pathway_issue_document_value_7_137 = pathway_issue_document_value_6_136["issue"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/issue", pathway_issue_document_value_7_137, None)
						
						# Retrieve value of data property: pathway_month_document
						pathway_month_document_value_0_138 = resource_data_1["MineralSystem"]
						pathway_month_document_index_1_139 = pathway_id_document_index_1_32
						pathway_month_document_value_1_140 = pathway_month_document_value_0_138[pathway_month_document_index_1_139]
						pathway_month_document_value_2_141 = pathway_month_document_value_1_140["pathway"]
						pathway_month_document_index_3_142 = pathway_id_document_index_3_37
						pathway_month_document_value_3_143 = pathway_month_document_value_2_141[pathway_month_document_index_3_142]
						if not ("supporting_references" in pathway_month_document_value_3_143):
							pass
						else:
							pathway_month_document_value_4_144 = pathway_month_document_value_3_143["supporting_references"]
							pathway_month_document_index_5_145 = pathway_id_document_index_5_42
							pathway_month_document_value_5_146 = pathway_month_document_value_4_144[pathway_month_document_index_5_145]
							if not ("document" in pathway_month_document_value_5_146):
								pass
							else:
								pathway_month_document_value_6_147 = pathway_month_document_value_5_146["document"]
								if not ("month" in pathway_month_document_value_6_147):
									pass
								else:
									pathway_month_document_value_7_148 = pathway_month_document_value_6_147["month"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/month", pathway_month_document_value_7_148, None)
						
						# Retrieve value of data property: pathway_year_document
						pathway_year_document_value_0_149 = resource_data_1["MineralSystem"]
						pathway_year_document_index_1_150 = pathway_id_document_index_1_32
						pathway_year_document_value_1_151 = pathway_year_document_value_0_149[pathway_year_document_index_1_150]
						pathway_year_document_value_2_152 = pathway_year_document_value_1_151["pathway"]
						pathway_year_document_index_3_153 = pathway_id_document_index_3_37
						pathway_year_document_value_3_154 = pathway_year_document_value_2_152[pathway_year_document_index_3_153]
						if not ("supporting_references" in pathway_year_document_value_3_154):
							pass
						else:
							pathway_year_document_value_4_155 = pathway_year_document_value_3_154["supporting_references"]
							pathway_year_document_index_5_156 = pathway_id_document_index_5_42
							pathway_year_document_value_5_157 = pathway_year_document_value_4_155[pathway_year_document_index_5_156]
							if not ("document" in pathway_year_document_value_5_157):
								pass
							else:
								pathway_year_document_value_6_158 = pathway_year_document_value_5_157["document"]
								if not ("year" in pathway_year_document_value_6_158):
									pass
								else:
									pathway_year_document_value_7_159 = pathway_year_document_value_6_158["year"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/year", pathway_year_document_value_7_159, None)
						
						writer_2.end_record()
	
	# Transform records of class mndr:BoundingBox:2
	pathway_x_min_value_0_160 = resource_data_1["MineralSystem"]
	start_161 = 0
	end_162 = len(pathway_x_min_value_0_160)
	for pathway_x_min_index_1_163 in range(start_161, end_162):
		pathway_x_min_value_1_164 = pathway_x_min_value_0_160[pathway_x_min_index_1_163]
		pathway_x_min_value_2_165 = pathway_x_min_value_1_164["pathway"]
		start_166 = 0
		end_167 = len(pathway_x_min_value_2_165)
		for pathway_x_min_index_3_168 in range(start_166, end_167):
			pathway_x_min_value_3_169 = pathway_x_min_value_2_165[pathway_x_min_index_3_168]
			if not ("supporting_references" in pathway_x_min_value_3_169):
				continue
			else:
				pathway_x_min_value_4_170 = pathway_x_min_value_3_169["supporting_references"]
				start_171 = 0
				end_172 = len(pathway_x_min_value_4_170)
				for pathway_x_min_index_5_173 in range(start_171, end_172):
					pathway_x_min_value_5_174 = pathway_x_min_value_4_170[pathway_x_min_index_5_173]
					if not ("page_info" in pathway_x_min_value_5_174):
						continue
					else:
						pathway_x_min_value_6_175 = pathway_x_min_value_5_174["page_info"]
						start_176 = 0
						end_177 = len(pathway_x_min_value_6_175)
						for pathway_x_min_index_7_178 in range(start_176, end_177):
							pathway_x_min_value_7_179 = pathway_x_min_value_6_175[pathway_x_min_index_7_178]
							if not ("bounding_box" in pathway_x_min_value_7_179):
								continue
							else:
								pathway_x_min_value_8_180 = pathway_x_min_value_7_179["bounding_box"]
								if not ("x_min" in pathway_x_min_value_8_180):
									continue
								else:
									pathway_x_min_value_9_181 = pathway_x_min_value_8_180["x_min"]
									writer_2.begin_record("https://minmod.isi.edu/resource/BoundingBox", (42, pathway_x_min_index_1_163, pathway_x_min_index_3_168, pathway_x_min_index_5_173, pathway_x_min_index_7_178), True, False)
									
									# Retrieve value of data property: pathway_x_min
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/x_min", pathway_x_min_value_9_181, None)
									
									# Retrieve value of data property: pathway_x_max
									pathway_x_max_value_0_182 = resource_data_1["MineralSystem"]
									pathway_x_max_index_1_183 = pathway_x_min_index_1_163
									pathway_x_max_value_1_184 = pathway_x_max_value_0_182[pathway_x_max_index_1_183]
									pathway_x_max_value_2_185 = pathway_x_max_value_1_184["pathway"]
									pathway_x_max_index_3_186 = pathway_x_min_index_3_168
									pathway_x_max_value_3_187 = pathway_x_max_value_2_185[pathway_x_max_index_3_186]
									if not ("supporting_references" in pathway_x_max_value_3_187):
										pass
									else:
										pathway_x_max_value_4_188 = pathway_x_max_value_3_187["supporting_references"]
										pathway_x_max_index_5_189 = pathway_x_min_index_5_173
										pathway_x_max_value_5_190 = pathway_x_max_value_4_188[pathway_x_max_index_5_189]
										if not ("page_info" in pathway_x_max_value_5_190):
											pass
										else:
											pathway_x_max_value_6_191 = pathway_x_max_value_5_190["page_info"]
											pathway_x_max_index_7_192 = pathway_x_min_index_7_178
											pathway_x_max_value_7_193 = pathway_x_max_value_6_191[pathway_x_max_index_7_192]
											if not ("bounding_box" in pathway_x_max_value_7_193):
												pass
											else:
												pathway_x_max_value_8_194 = pathway_x_max_value_7_193["bounding_box"]
												if not ("x_max" in pathway_x_max_value_8_194):
													pass
												else:
													pathway_x_max_value_9_195 = pathway_x_max_value_8_194["x_max"]
													if True:
														writer_2.write_data_property("https://minmod.isi.edu/resource/x_max", pathway_x_max_value_9_195, None)
									
									# Retrieve value of data property: pathway_y_min
									pathway_y_min_value_0_196 = resource_data_1["MineralSystem"]
									pathway_y_min_index_1_197 = pathway_x_min_index_1_163
									pathway_y_min_value_1_198 = pathway_y_min_value_0_196[pathway_y_min_index_1_197]
									pathway_y_min_value_2_199 = pathway_y_min_value_1_198["pathway"]
									pathway_y_min_index_3_200 = pathway_x_min_index_3_168
									pathway_y_min_value_3_201 = pathway_y_min_value_2_199[pathway_y_min_index_3_200]
									if not ("supporting_references" in pathway_y_min_value_3_201):
										pass
									else:
										pathway_y_min_value_4_202 = pathway_y_min_value_3_201["supporting_references"]
										pathway_y_min_index_5_203 = pathway_x_min_index_5_173
										pathway_y_min_value_5_204 = pathway_y_min_value_4_202[pathway_y_min_index_5_203]
										if not ("page_info" in pathway_y_min_value_5_204):
											pass
										else:
											pathway_y_min_value_6_205 = pathway_y_min_value_5_204["page_info"]
											pathway_y_min_index_7_206 = pathway_x_min_index_7_178
											pathway_y_min_value_7_207 = pathway_y_min_value_6_205[pathway_y_min_index_7_206]
											if not ("bounding_box" in pathway_y_min_value_7_207):
												pass
											else:
												pathway_y_min_value_8_208 = pathway_y_min_value_7_207["bounding_box"]
												if not ("y_min" in pathway_y_min_value_8_208):
													pass
												else:
													pathway_y_min_value_9_209 = pathway_y_min_value_8_208["y_min"]
													if True:
														writer_2.write_data_property("https://minmod.isi.edu/resource/y_min", pathway_y_min_value_9_209, None)
									
									# Retrieve value of data property: pathway_y_max
									pathway_y_max_value_0_210 = resource_data_1["MineralSystem"]
									pathway_y_max_index_1_211 = pathway_x_min_index_1_163
									pathway_y_max_value_1_212 = pathway_y_max_value_0_210[pathway_y_max_index_1_211]
									pathway_y_max_value_2_213 = pathway_y_max_value_1_212["pathway"]
									pathway_y_max_index_3_214 = pathway_x_min_index_3_168
									pathway_y_max_value_3_215 = pathway_y_max_value_2_213[pathway_y_max_index_3_214]
									if not ("supporting_references" in pathway_y_max_value_3_215):
										pass
									else:
										pathway_y_max_value_4_216 = pathway_y_max_value_3_215["supporting_references"]
										pathway_y_max_index_5_217 = pathway_x_min_index_5_173
										pathway_y_max_value_5_218 = pathway_y_max_value_4_216[pathway_y_max_index_5_217]
										if not ("page_info" in pathway_y_max_value_5_218):
											pass
										else:
											pathway_y_max_value_6_219 = pathway_y_max_value_5_218["page_info"]
											pathway_y_max_index_7_220 = pathway_x_min_index_7_178
											pathway_y_max_value_7_221 = pathway_y_max_value_6_219[pathway_y_max_index_7_220]
											if not ("bounding_box" in pathway_y_max_value_7_221):
												pass
											else:
												pathway_y_max_value_8_222 = pathway_y_max_value_7_221["bounding_box"]
												if not ("y_max" in pathway_y_max_value_8_222):
													pass
												else:
													pathway_y_max_value_9_223 = pathway_y_max_value_8_222["y_max"]
													if True:
														writer_2.write_data_property("https://minmod.isi.edu/resource/y_max", pathway_y_max_value_9_223, None)
									
									writer_2.end_record()
	
	# Transform records of class mndr:PageInfo:2
	pathway_page_value_0_224 = resource_data_1["MineralSystem"]
	start_225 = 0
	end_226 = len(pathway_page_value_0_224)
	for pathway_page_index_1_227 in range(start_225, end_226):
		pathway_page_value_1_228 = pathway_page_value_0_224[pathway_page_index_1_227]
		pathway_page_value_2_229 = pathway_page_value_1_228["pathway"]
		start_230 = 0
		end_231 = len(pathway_page_value_2_229)
		for pathway_page_index_3_232 in range(start_230, end_231):
			pathway_page_value_3_233 = pathway_page_value_2_229[pathway_page_index_3_232]
			if not ("supporting_references" in pathway_page_value_3_233):
				continue
			else:
				pathway_page_value_4_234 = pathway_page_value_3_233["supporting_references"]
				start_235 = 0
				end_236 = len(pathway_page_value_4_234)
				for pathway_page_index_5_237 in range(start_235, end_236):
					pathway_page_value_5_238 = pathway_page_value_4_234[pathway_page_index_5_237]
					if not ("page_info" in pathway_page_value_5_238):
						continue
					else:
						pathway_page_value_6_239 = pathway_page_value_5_238["page_info"]
						start_240 = 0
						end_241 = len(pathway_page_value_6_239)
						for pathway_page_index_7_242 in range(start_240, end_241):
							pathway_page_value_7_243 = pathway_page_value_6_239[pathway_page_index_7_242]
							if not ("page" in pathway_page_value_7_243):
								continue
							else:
								pathway_page_value_8_244 = pathway_page_value_7_243["page"]
								writer_2.begin_record("https://minmod.isi.edu/resource/PageInfo", (40, pathway_page_index_1_227, pathway_page_index_3_232, pathway_page_index_5_237, pathway_page_index_7_242), True, False)
								
								# Retrieve value of data property: pathway_page
								if True:
									writer_2.write_data_property("https://minmod.isi.edu/resource/page", pathway_page_value_8_244, None)
								
								# Retrieve value of object property: pathway_x_min
								pathway_x_min_value_0_245 = resource_data_1["MineralSystem"]
								pathway_x_min_index_1_246 = pathway_page_index_1_227
								pathway_x_min_value_1_247 = pathway_x_min_value_0_245[pathway_x_min_index_1_246]
								pathway_x_min_value_2_248 = pathway_x_min_value_1_247["pathway"]
								pathway_x_min_index_3_249 = pathway_page_index_3_232
								pathway_x_min_value_3_250 = pathway_x_min_value_2_248[pathway_x_min_index_3_249]
								if not ("supporting_references" in pathway_x_min_value_3_250):
									pass
								else:
									pathway_x_min_value_4_251 = pathway_x_min_value_3_250["supporting_references"]
									pathway_x_min_index_5_252 = pathway_page_index_5_237
									pathway_x_min_value_5_253 = pathway_x_min_value_4_251[pathway_x_min_index_5_252]
									if not ("page_info" in pathway_x_min_value_5_253):
										pass
									else:
										pathway_x_min_value_6_254 = pathway_x_min_value_5_253["page_info"]
										pathway_x_min_index_7_255 = pathway_page_index_7_242
										pathway_x_min_value_7_256 = pathway_x_min_value_6_254[pathway_x_min_index_7_255]
										if not ("bounding_box" in pathway_x_min_value_7_256):
											pass
										else:
											pathway_x_min_value_8_257 = pathway_x_min_value_7_256["bounding_box"]
											if not ("x_min" in pathway_x_min_value_8_257):
												pass
											else:
												pathway_x_min_value_9_258 = pathway_x_min_value_8_257["x_min"]
												if writer_2.has_written_record((42, pathway_x_min_index_1_246, pathway_x_min_index_3_249, pathway_x_min_index_5_252, pathway_x_min_index_7_255)):
													writer_2.write_object_property("https://minmod.isi.edu/resource/bounding_box", (42, pathway_x_min_index_1_246, pathway_x_min_index_3_249, pathway_x_min_index_5_252, pathway_x_min_index_7_255), True, True, False)
								
								writer_2.end_record()
	
	# Transform records of class mndr:Reference:2
	pathway_id_document_value_0_259 = resource_data_1["MineralSystem"]
	start_260 = 0
	end_261 = len(pathway_id_document_value_0_259)
	for pathway_id_document_index_1_262 in range(start_260, end_261):
		pathway_id_document_value_1_263 = pathway_id_document_value_0_259[pathway_id_document_index_1_262]
		pathway_id_document_value_2_264 = pathway_id_document_value_1_263["pathway"]
		start_265 = 0
		end_266 = len(pathway_id_document_value_2_264)
		for pathway_id_document_index_3_267 in range(start_265, end_266):
			pathway_id_document_value_3_268 = pathway_id_document_value_2_264[pathway_id_document_index_3_267]
			if not ("supporting_references" in pathway_id_document_value_3_268):
				continue
			else:
				pathway_id_document_value_4_269 = pathway_id_document_value_3_268["supporting_references"]
				start_270 = 0
				end_271 = len(pathway_id_document_value_4_269)
				for pathway_id_document_index_5_272 in range(start_270, end_271):
					pathway_id_document_value_5_273 = pathway_id_document_value_4_269[pathway_id_document_index_5_272]
					if not ("document" in pathway_id_document_value_5_273):
						continue
					else:
						pathway_id_document_value_6_274 = pathway_id_document_value_5_273["document"]
						pathway_id_document_value_7_275 = pathway_id_document_value_6_274["id"]
						writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (30, pathway_id_document_index_1_262, pathway_id_document_index_3_267, pathway_id_document_index_5_272), True, False)
						
						# Retrieve value of data property: pathway_id_document
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/document_id", pathway_id_document_value_7_275, None)
						
						# Retrieve value of object property: pathway_id_document
						if writer_2.has_written_record(pathway_id_document_value_7_275):
							writer_2.write_object_property("https://minmod.isi.edu/resource/document", pathway_id_document_value_7_275, True, False, False)
						
						# Retrieve value of object property: pathway_page
						pathway_page_value_0_276 = resource_data_1["MineralSystem"]
						pathway_page_index_1_277 = pathway_id_document_index_1_262
						pathway_page_value_1_278 = pathway_page_value_0_276[pathway_page_index_1_277]
						pathway_page_value_2_279 = pathway_page_value_1_278["pathway"]
						pathway_page_index_3_280 = pathway_id_document_index_3_267
						pathway_page_value_3_281 = pathway_page_value_2_279[pathway_page_index_3_280]
						if not ("supporting_references" in pathway_page_value_3_281):
							pass
						else:
							pathway_page_value_4_282 = pathway_page_value_3_281["supporting_references"]
							pathway_page_index_5_283 = pathway_id_document_index_5_272
							pathway_page_value_5_284 = pathway_page_value_4_282[pathway_page_index_5_283]
							if not ("page_info" in pathway_page_value_5_284):
								pass
							else:
								pathway_page_value_6_285 = pathway_page_value_5_284["page_info"]
								start_286 = 0
								end_287 = len(pathway_page_value_6_285)
								for pathway_page_index_7_288 in range(start_286, end_287):
									pathway_page_value_7_289 = pathway_page_value_6_285[pathway_page_index_7_288]
									if not ("page" in pathway_page_value_7_289):
										pass
									else:
										pathway_page_value_8_290 = pathway_page_value_7_289["page"]
										if writer_2.has_written_record((40, pathway_page_index_1_277, pathway_page_index_3_280, pathway_page_index_5_283, pathway_page_index_7_288)):
											writer_2.write_object_property("https://minmod.isi.edu/resource/page_info", (40, pathway_page_index_1_277, pathway_page_index_3_280, pathway_page_index_5_283, pathway_page_index_7_288), True, True, False)
						
						writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:2
	pathway_criteria_value_0_291 = resource_data_1["MineralSystem"]
	start_292 = 0
	end_293 = len(pathway_criteria_value_0_291)
	for pathway_criteria_index_1_294 in range(start_292, end_293):
		pathway_criteria_value_1_295 = pathway_criteria_value_0_291[pathway_criteria_index_1_294]
		pathway_criteria_value_2_296 = pathway_criteria_value_1_295["pathway"]
		start_297 = 0
		end_298 = len(pathway_criteria_value_2_296)
		for pathway_criteria_index_3_299 in range(start_297, end_298):
			pathway_criteria_value_3_300 = pathway_criteria_value_2_296[pathway_criteria_index_3_299]
			pathway_criteria_value_4_301 = pathway_criteria_value_3_300["criteria"]
			writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (24, pathway_criteria_index_1_294, pathway_criteria_index_3_299), True, False)
			
			# Retrieve value of data property: pathway_criteria
			writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", pathway_criteria_value_4_301, None)
			
			# Retrieve value of data property: pathway_theoretical
			pathway_theoretical_value_0_302 = resource_data_1["MineralSystem"]
			pathway_theoretical_index_1_303 = pathway_criteria_index_1_294
			pathway_theoretical_value_1_304 = pathway_theoretical_value_0_302[pathway_theoretical_index_1_303]
			pathway_theoretical_value_2_305 = pathway_theoretical_value_1_304["pathway"]
			pathway_theoretical_index_3_306 = pathway_criteria_index_3_299
			pathway_theoretical_value_3_307 = pathway_theoretical_value_2_305[pathway_theoretical_index_3_306]
			if not ("theoretical" in pathway_theoretical_value_3_307):
				pass
			else:
				pathway_theoretical_value_4_308 = pathway_theoretical_value_3_307["theoretical"]
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/theoretical", pathway_theoretical_value_4_308, None)
			
			# Retrieve value of object property: pathway_potential_dataset_name
			pathway_potential_dataset_name_value_0_309 = resource_data_1["MineralSystem"]
			pathway_potential_dataset_name_index_1_310 = pathway_criteria_index_1_294
			pathway_potential_dataset_name_value_1_311 = pathway_potential_dataset_name_value_0_309[pathway_potential_dataset_name_index_1_310]
			pathway_potential_dataset_name_value_2_312 = pathway_potential_dataset_name_value_1_311["pathway"]
			pathway_potential_dataset_name_index_3_313 = pathway_criteria_index_3_299
			pathway_potential_dataset_name_value_3_314 = pathway_potential_dataset_name_value_2_312[pathway_potential_dataset_name_index_3_313]
			if not ("potential_dataset" in pathway_potential_dataset_name_value_3_314):
				pass
			else:
				pathway_potential_dataset_name_value_4_315 = pathway_potential_dataset_name_value_3_314["potential_dataset"]
				start_316 = 0
				end_317 = len(pathway_potential_dataset_name_value_4_315)
				for pathway_potential_dataset_name_index_5_318 in range(start_316, end_317):
					pathway_potential_dataset_name_value_5_319 = pathway_potential_dataset_name_value_4_315[pathway_potential_dataset_name_index_5_318]
					pathway_potential_dataset_name_value_6_320 = pathway_potential_dataset_name_value_5_319["name"]
					if writer_2.has_written_record((26, pathway_potential_dataset_name_index_1_310, pathway_potential_dataset_name_index_3_313, pathway_potential_dataset_name_index_5_318)):
						writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (26, pathway_potential_dataset_name_index_1_310, pathway_potential_dataset_name_index_3_313, pathway_potential_dataset_name_index_5_318), True, True, False)
			
			# Retrieve value of object property: pathway_id_document
			pathway_id_document_value_0_321 = resource_data_1["MineralSystem"]
			pathway_id_document_index_1_322 = pathway_criteria_index_1_294
			pathway_id_document_value_1_323 = pathway_id_document_value_0_321[pathway_id_document_index_1_322]
			pathway_id_document_value_2_324 = pathway_id_document_value_1_323["pathway"]
			pathway_id_document_index_3_325 = pathway_criteria_index_3_299
			pathway_id_document_value_3_326 = pathway_id_document_value_2_324[pathway_id_document_index_3_325]
			if not ("supporting_references" in pathway_id_document_value_3_326):
				pass
			else:
				pathway_id_document_value_4_327 = pathway_id_document_value_3_326["supporting_references"]
				start_328 = 0
				end_329 = len(pathway_id_document_value_4_327)
				for pathway_id_document_index_5_330 in range(start_328, end_329):
					pathway_id_document_value_5_331 = pathway_id_document_value_4_327[pathway_id_document_index_5_330]
					if not ("document" in pathway_id_document_value_5_331):
						pass
					else:
						pathway_id_document_value_6_332 = pathway_id_document_value_5_331["document"]
						pathway_id_document_value_7_333 = pathway_id_document_value_6_332["id"]
						if writer_2.has_written_record((30, pathway_id_document_index_1_322, pathway_id_document_index_3_325, pathway_id_document_index_5_330)):
							writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (30, pathway_id_document_index_1_322, pathway_id_document_index_3_325, pathway_id_document_index_5_330), True, True, False)
			
			writer_2.end_record()
	
	# Transform records of class mndr:EvidenceLayer:3
	trap_potential_dataset_name_value_0_334 = resource_data_1["MineralSystem"]
	start_335 = 0
	end_336 = len(trap_potential_dataset_name_value_0_334)
	for trap_potential_dataset_name_index_1_337 in range(start_335, end_336):
		trap_potential_dataset_name_value_1_338 = trap_potential_dataset_name_value_0_334[trap_potential_dataset_name_index_1_337]
		if not ("trap" in trap_potential_dataset_name_value_1_338):
			continue
		else:
			trap_potential_dataset_name_value_2_339 = trap_potential_dataset_name_value_1_338["trap"]
			start_340 = 0
			end_341 = len(trap_potential_dataset_name_value_2_339)
			for trap_potential_dataset_name_index_3_342 in range(start_340, end_341):
				trap_potential_dataset_name_value_3_343 = trap_potential_dataset_name_value_2_339[trap_potential_dataset_name_index_3_342]
				if not ("potential_dataset" in trap_potential_dataset_name_value_3_343):
					continue
				else:
					trap_potential_dataset_name_value_4_344 = trap_potential_dataset_name_value_3_343["potential_dataset"]
					start_345 = 0
					end_346 = len(trap_potential_dataset_name_value_4_344)
					for trap_potential_dataset_name_index_5_347 in range(start_345, end_346):
						trap_potential_dataset_name_value_5_348 = trap_potential_dataset_name_value_4_344[trap_potential_dataset_name_index_5_347]
						trap_potential_dataset_name_value_6_349 = trap_potential_dataset_name_value_5_348["name"]
						writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (48, trap_potential_dataset_name_index_1_337, trap_potential_dataset_name_index_3_342, trap_potential_dataset_name_index_5_347), True, False)
						
						# Retrieve value of data property: trap_potential_dataset_name
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/name", trap_potential_dataset_name_value_6_349, None)
						
						# Retrieve value of data property: trap_potential_dataset_score
						trap_potential_dataset_score_value_0_350 = resource_data_1["MineralSystem"]
						trap_potential_dataset_score_index_1_351 = trap_potential_dataset_name_index_1_337
						trap_potential_dataset_score_value_1_352 = trap_potential_dataset_score_value_0_350[trap_potential_dataset_score_index_1_351]
						if not ("trap" in trap_potential_dataset_score_value_1_352):
							pass
						else:
							trap_potential_dataset_score_value_2_353 = trap_potential_dataset_score_value_1_352["trap"]
							trap_potential_dataset_score_index_3_354 = trap_potential_dataset_name_index_3_342
							trap_potential_dataset_score_value_3_355 = trap_potential_dataset_score_value_2_353[trap_potential_dataset_score_index_3_354]
							if not ("potential_dataset" in trap_potential_dataset_score_value_3_355):
								pass
							else:
								trap_potential_dataset_score_value_4_356 = trap_potential_dataset_score_value_3_355["potential_dataset"]
								trap_potential_dataset_score_index_5_357 = trap_potential_dataset_name_index_5_347
								trap_potential_dataset_score_value_5_358 = trap_potential_dataset_score_value_4_356[trap_potential_dataset_score_index_5_357]
								trap_potential_dataset_score_value_6_359 = trap_potential_dataset_score_value_5_358["relevance_score"]
								if True:
									writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", trap_potential_dataset_score_value_6_359, None)
						
						writer_2.end_record()
	
	# Transform records of class mndr:Document:3
	trap_id_document_value_0_360 = resource_data_1["MineralSystem"]
	start_361 = 0
	end_362 = len(trap_id_document_value_0_360)
	for trap_id_document_index_1_363 in range(start_361, end_362):
		trap_id_document_value_1_364 = trap_id_document_value_0_360[trap_id_document_index_1_363]
		if not ("trap" in trap_id_document_value_1_364):
			continue
		else:
			trap_id_document_value_2_365 = trap_id_document_value_1_364["trap"]
			start_366 = 0
			end_367 = len(trap_id_document_value_2_365)
			for trap_id_document_index_3_368 in range(start_366, end_367):
				trap_id_document_value_3_369 = trap_id_document_value_2_365[trap_id_document_index_3_368]
				if not ("supporting_references" in trap_id_document_value_3_369):
					continue
				else:
					trap_id_document_value_4_370 = trap_id_document_value_3_369["supporting_references"]
					start_371 = 0
					end_372 = len(trap_id_document_value_4_370)
					for trap_id_document_index_5_373 in range(start_371, end_372):
						trap_id_document_value_5_374 = trap_id_document_value_4_370[trap_id_document_index_5_373]
						if not ("document" in trap_id_document_value_5_374):
							continue
						else:
							trap_id_document_value_6_375 = trap_id_document_value_5_374["document"]
							trap_id_document_value_7_376 = trap_id_document_value_6_375["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Document", trap_id_document_value_7_376, False, False)
							
							# Retrieve value of data property: trap_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/id", trap_id_document_value_7_376, None)
							
							# Retrieve value of data property: trap_uri_document
							trap_uri_document_value_0_377 = resource_data_1["MineralSystem"]
							trap_uri_document_index_1_378 = trap_id_document_index_1_363
							trap_uri_document_value_1_379 = trap_uri_document_value_0_377[trap_uri_document_index_1_378]
							if not ("trap" in trap_uri_document_value_1_379):
								pass
							else:
								trap_uri_document_value_2_380 = trap_uri_document_value_1_379["trap"]
								trap_uri_document_index_3_381 = trap_id_document_index_3_368
								trap_uri_document_value_3_382 = trap_uri_document_value_2_380[trap_uri_document_index_3_381]
								if not ("supporting_references" in trap_uri_document_value_3_382):
									pass
								else:
									trap_uri_document_value_4_383 = trap_uri_document_value_3_382["supporting_references"]
									trap_uri_document_index_5_384 = trap_id_document_index_5_373
									trap_uri_document_value_5_385 = trap_uri_document_value_4_383[trap_uri_document_index_5_384]
									if not ("document" in trap_uri_document_value_5_385):
										pass
									else:
										trap_uri_document_value_6_386 = trap_uri_document_value_5_385["document"]
										if not ("uri" in trap_uri_document_value_6_386):
											pass
										else:
											trap_uri_document_value_7_387 = trap_uri_document_value_6_386["uri"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/uri", trap_uri_document_value_7_387, None)
							
							# Retrieve value of data property: trap_doi
							trap_doi_value_0_388 = resource_data_1["MineralSystem"]
							trap_doi_index_1_389 = trap_id_document_index_1_363
							trap_doi_value_1_390 = trap_doi_value_0_388[trap_doi_index_1_389]
							if not ("trap" in trap_doi_value_1_390):
								pass
							else:
								trap_doi_value_2_391 = trap_doi_value_1_390["trap"]
								trap_doi_index_3_392 = trap_id_document_index_3_368
								trap_doi_value_3_393 = trap_doi_value_2_391[trap_doi_index_3_392]
								if not ("supporting_references" in trap_doi_value_3_393):
									pass
								else:
									trap_doi_value_4_394 = trap_doi_value_3_393["supporting_references"]
									trap_doi_index_5_395 = trap_id_document_index_5_373
									trap_doi_value_5_396 = trap_doi_value_4_394[trap_doi_index_5_395]
									if not ("document" in trap_doi_value_5_396):
										pass
									else:
										trap_doi_value_6_397 = trap_doi_value_5_396["document"]
										if not ("doi" in trap_doi_value_6_397):
											pass
										else:
											trap_doi_value_7_398 = trap_doi_value_6_397["doi"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/doi", trap_doi_value_7_398, None)
							
							# Retrieve value of data property: trap_journal
							trap_journal_value_0_399 = resource_data_1["MineralSystem"]
							trap_journal_index_1_400 = trap_id_document_index_1_363
							trap_journal_value_1_401 = trap_journal_value_0_399[trap_journal_index_1_400]
							if not ("trap" in trap_journal_value_1_401):
								pass
							else:
								trap_journal_value_2_402 = trap_journal_value_1_401["trap"]
								trap_journal_index_3_403 = trap_id_document_index_3_368
								trap_journal_value_3_404 = trap_journal_value_2_402[trap_journal_index_3_403]
								if not ("supporting_references" in trap_journal_value_3_404):
									pass
								else:
									trap_journal_value_4_405 = trap_journal_value_3_404["supporting_references"]
									trap_journal_index_5_406 = trap_id_document_index_5_373
									trap_journal_value_5_407 = trap_journal_value_4_405[trap_journal_index_5_406]
									if not ("document" in trap_journal_value_5_407):
										pass
									else:
										trap_journal_value_6_408 = trap_journal_value_5_407["document"]
										if not ("journal" in trap_journal_value_6_408):
											pass
										else:
											trap_journal_value_7_409 = trap_journal_value_6_408["journal"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/journal", trap_journal_value_7_409, None)
							
							# Retrieve value of data property: trap_authors
							trap_authors_value_0_410 = resource_data_1["MineralSystem"]
							trap_authors_index_1_411 = trap_id_document_index_1_363
							trap_authors_value_1_412 = trap_authors_value_0_410[trap_authors_index_1_411]
							if not ("trap" in trap_authors_value_1_412):
								pass
							else:
								trap_authors_value_2_413 = trap_authors_value_1_412["trap"]
								trap_authors_index_3_414 = trap_id_document_index_3_368
								trap_authors_value_3_415 = trap_authors_value_2_413[trap_authors_index_3_414]
								if not ("supporting_references" in trap_authors_value_3_415):
									pass
								else:
									trap_authors_value_4_416 = trap_authors_value_3_415["supporting_references"]
									trap_authors_index_5_417 = trap_id_document_index_5_373
									trap_authors_value_5_418 = trap_authors_value_4_416[trap_authors_index_5_417]
									if not ("document" in trap_authors_value_5_418):
										pass
									else:
										trap_authors_value_6_419 = trap_authors_value_5_418["document"]
										if not ("authors" in trap_authors_value_6_419):
											pass
										else:
											trap_authors_value_7_420 = trap_authors_value_6_419["authors"]
											start_421 = 0
											end_422 = len(trap_authors_value_7_420)
											for trap_authors_index_8_423 in range(start_421, end_422):
												trap_authors_value_8_424 = trap_authors_value_7_420[trap_authors_index_8_423]
												if True:
													writer_2.write_data_property("https://minmod.isi.edu/resource/authors", trap_authors_value_8_424, None)
							
							# Retrieve value of data property: trap_description_document
							trap_description_document_value_0_425 = resource_data_1["MineralSystem"]
							trap_description_document_index_1_426 = trap_id_document_index_1_363
							trap_description_document_value_1_427 = trap_description_document_value_0_425[trap_description_document_index_1_426]
							if not ("trap" in trap_description_document_value_1_427):
								pass
							else:
								trap_description_document_value_2_428 = trap_description_document_value_1_427["trap"]
								trap_description_document_index_3_429 = trap_id_document_index_3_368
								trap_description_document_value_3_430 = trap_description_document_value_2_428[trap_description_document_index_3_429]
								if not ("supporting_references" in trap_description_document_value_3_430):
									pass
								else:
									trap_description_document_value_4_431 = trap_description_document_value_3_430["supporting_references"]
									trap_description_document_index_5_432 = trap_id_document_index_5_373
									trap_description_document_value_5_433 = trap_description_document_value_4_431[trap_description_document_index_5_432]
									if not ("document" in trap_description_document_value_5_433):
										pass
									else:
										trap_description_document_value_6_434 = trap_description_document_value_5_433["document"]
										if not ("description" in trap_description_document_value_6_434):
											pass
										else:
											trap_description_document_value_7_435 = trap_description_document_value_6_434["description"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/description", trap_description_document_value_7_435, None)
							
							# Retrieve value of data property: trap_title_document
							trap_title_document_value_0_436 = resource_data_1["MineralSystem"]
							trap_title_document_index_1_437 = trap_id_document_index_1_363
							trap_title_document_value_1_438 = trap_title_document_value_0_436[trap_title_document_index_1_437]
							if not ("trap" in trap_title_document_value_1_438):
								pass
							else:
								trap_title_document_value_2_439 = trap_title_document_value_1_438["trap"]
								trap_title_document_index_3_440 = trap_id_document_index_3_368
								trap_title_document_value_3_441 = trap_title_document_value_2_439[trap_title_document_index_3_440]
								if not ("supporting_references" in trap_title_document_value_3_441):
									pass
								else:
									trap_title_document_value_4_442 = trap_title_document_value_3_441["supporting_references"]
									trap_title_document_index_5_443 = trap_id_document_index_5_373
									trap_title_document_value_5_444 = trap_title_document_value_4_442[trap_title_document_index_5_443]
									if not ("document" in trap_title_document_value_5_444):
										pass
									else:
										trap_title_document_value_6_445 = trap_title_document_value_5_444["document"]
										if not ("title" in trap_title_document_value_6_445):
											pass
										else:
											trap_title_document_value_7_446 = trap_title_document_value_6_445["title"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/title", trap_title_document_value_7_446, None)
							
							# Retrieve value of data property: trap_volume
							trap_volume_value_0_447 = resource_data_1["MineralSystem"]
							trap_volume_index_1_448 = trap_id_document_index_1_363
							trap_volume_value_1_449 = trap_volume_value_0_447[trap_volume_index_1_448]
							if not ("trap" in trap_volume_value_1_449):
								pass
							else:
								trap_volume_value_2_450 = trap_volume_value_1_449["trap"]
								trap_volume_index_3_451 = trap_id_document_index_3_368
								trap_volume_value_3_452 = trap_volume_value_2_450[trap_volume_index_3_451]
								if not ("supporting_references" in trap_volume_value_3_452):
									pass
								else:
									trap_volume_value_4_453 = trap_volume_value_3_452["supporting_references"]
									trap_volume_index_5_454 = trap_id_document_index_5_373
									trap_volume_value_5_455 = trap_volume_value_4_453[trap_volume_index_5_454]
									if not ("document" in trap_volume_value_5_455):
										pass
									else:
										trap_volume_value_6_456 = trap_volume_value_5_455["document"]
										if not ("volume" in trap_volume_value_6_456):
											pass
										else:
											trap_volume_value_7_457 = trap_volume_value_6_456["volume"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/volume", trap_volume_value_7_457, None)
							
							# Retrieve value of data property: trap_issue_document
							trap_issue_document_value_0_458 = resource_data_1["MineralSystem"]
							trap_issue_document_index_1_459 = trap_id_document_index_1_363
							trap_issue_document_value_1_460 = trap_issue_document_value_0_458[trap_issue_document_index_1_459]
							if not ("trap" in trap_issue_document_value_1_460):
								pass
							else:
								trap_issue_document_value_2_461 = trap_issue_document_value_1_460["trap"]
								trap_issue_document_index_3_462 = trap_id_document_index_3_368
								trap_issue_document_value_3_463 = trap_issue_document_value_2_461[trap_issue_document_index_3_462]
								if not ("supporting_references" in trap_issue_document_value_3_463):
									pass
								else:
									trap_issue_document_value_4_464 = trap_issue_document_value_3_463["supporting_references"]
									trap_issue_document_index_5_465 = trap_id_document_index_5_373
									trap_issue_document_value_5_466 = trap_issue_document_value_4_464[trap_issue_document_index_5_465]
									if not ("document" in trap_issue_document_value_5_466):
										pass
									else:
										trap_issue_document_value_6_467 = trap_issue_document_value_5_466["document"]
										if not ("issue" in trap_issue_document_value_6_467):
											pass
										else:
											trap_issue_document_value_7_468 = trap_issue_document_value_6_467["issue"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/issue", trap_issue_document_value_7_468, None)
							
							# Retrieve value of data property: trap_month_document
							trap_month_document_value_0_469 = resource_data_1["MineralSystem"]
							trap_month_document_index_1_470 = trap_id_document_index_1_363
							trap_month_document_value_1_471 = trap_month_document_value_0_469[trap_month_document_index_1_470]
							if not ("trap" in trap_month_document_value_1_471):
								pass
							else:
								trap_month_document_value_2_472 = trap_month_document_value_1_471["trap"]
								trap_month_document_index_3_473 = trap_id_document_index_3_368
								trap_month_document_value_3_474 = trap_month_document_value_2_472[trap_month_document_index_3_473]
								if not ("supporting_references" in trap_month_document_value_3_474):
									pass
								else:
									trap_month_document_value_4_475 = trap_month_document_value_3_474["supporting_references"]
									trap_month_document_index_5_476 = trap_id_document_index_5_373
									trap_month_document_value_5_477 = trap_month_document_value_4_475[trap_month_document_index_5_476]
									if not ("document" in trap_month_document_value_5_477):
										pass
									else:
										trap_month_document_value_6_478 = trap_month_document_value_5_477["document"]
										if not ("month" in trap_month_document_value_6_478):
											pass
										else:
											trap_month_document_value_7_479 = trap_month_document_value_6_478["month"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/month", trap_month_document_value_7_479, None)
							
							# Retrieve value of data property: trap_year_document
							trap_year_document_value_0_480 = resource_data_1["MineralSystem"]
							trap_year_document_index_1_481 = trap_id_document_index_1_363
							trap_year_document_value_1_482 = trap_year_document_value_0_480[trap_year_document_index_1_481]
							if not ("trap" in trap_year_document_value_1_482):
								pass
							else:
								trap_year_document_value_2_483 = trap_year_document_value_1_482["trap"]
								trap_year_document_index_3_484 = trap_id_document_index_3_368
								trap_year_document_value_3_485 = trap_year_document_value_2_483[trap_year_document_index_3_484]
								if not ("supporting_references" in trap_year_document_value_3_485):
									pass
								else:
									trap_year_document_value_4_486 = trap_year_document_value_3_485["supporting_references"]
									trap_year_document_index_5_487 = trap_id_document_index_5_373
									trap_year_document_value_5_488 = trap_year_document_value_4_486[trap_year_document_index_5_487]
									if not ("document" in trap_year_document_value_5_488):
										pass
									else:
										trap_year_document_value_6_489 = trap_year_document_value_5_488["document"]
										if not ("year" in trap_year_document_value_6_489):
											pass
										else:
											trap_year_document_value_7_490 = trap_year_document_value_6_489["year"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/year", trap_year_document_value_7_490, None)
							
							writer_2.end_record()
	
	# Transform records of class mndr:BoundingBox:3
	trap_x_min_value_0_491 = resource_data_1["MineralSystem"]
	start_492 = 0
	end_493 = len(trap_x_min_value_0_491)
	for trap_x_min_index_1_494 in range(start_492, end_493):
		trap_x_min_value_1_495 = trap_x_min_value_0_491[trap_x_min_index_1_494]
		if not ("trap" in trap_x_min_value_1_495):
			continue
		else:
			trap_x_min_value_2_496 = trap_x_min_value_1_495["trap"]
			start_497 = 0
			end_498 = len(trap_x_min_value_2_496)
			for trap_x_min_index_3_499 in range(start_497, end_498):
				trap_x_min_value_3_500 = trap_x_min_value_2_496[trap_x_min_index_3_499]
				if not ("supporting_references" in trap_x_min_value_3_500):
					continue
				else:
					trap_x_min_value_4_501 = trap_x_min_value_3_500["supporting_references"]
					start_502 = 0
					end_503 = len(trap_x_min_value_4_501)
					for trap_x_min_index_5_504 in range(start_502, end_503):
						trap_x_min_value_5_505 = trap_x_min_value_4_501[trap_x_min_index_5_504]
						if not ("page_info" in trap_x_min_value_5_505):
							continue
						else:
							trap_x_min_value_6_506 = trap_x_min_value_5_505["page_info"]
							start_507 = 0
							end_508 = len(trap_x_min_value_6_506)
							for trap_x_min_index_7_509 in range(start_507, end_508):
								trap_x_min_value_7_510 = trap_x_min_value_6_506[trap_x_min_index_7_509]
								if not ("bounding_box" in trap_x_min_value_7_510):
									continue
								else:
									trap_x_min_value_8_511 = trap_x_min_value_7_510["bounding_box"]
									if not ("x_min" in trap_x_min_value_8_511):
										continue
									else:
										trap_x_min_value_9_512 = trap_x_min_value_8_511["x_min"]
										writer_2.begin_record("https://minmod.isi.edu/resource/BoundingBox", (64, trap_x_min_index_1_494, trap_x_min_index_3_499, trap_x_min_index_5_504, trap_x_min_index_7_509), True, False)
										
										# Retrieve value of data property: trap_x_min
										if True:
											writer_2.write_data_property("https://minmod.isi.edu/resource/x_min", trap_x_min_value_9_512, None)
										
										# Retrieve value of data property: trap_x_max
										trap_x_max_value_0_513 = resource_data_1["MineralSystem"]
										trap_x_max_index_1_514 = trap_x_min_index_1_494
										trap_x_max_value_1_515 = trap_x_max_value_0_513[trap_x_max_index_1_514]
										if not ("trap" in trap_x_max_value_1_515):
											pass
										else:
											trap_x_max_value_2_516 = trap_x_max_value_1_515["trap"]
											trap_x_max_index_3_517 = trap_x_min_index_3_499
											trap_x_max_value_3_518 = trap_x_max_value_2_516[trap_x_max_index_3_517]
											if not ("supporting_references" in trap_x_max_value_3_518):
												pass
											else:
												trap_x_max_value_4_519 = trap_x_max_value_3_518["supporting_references"]
												trap_x_max_index_5_520 = trap_x_min_index_5_504
												trap_x_max_value_5_521 = trap_x_max_value_4_519[trap_x_max_index_5_520]
												if not ("page_info" in trap_x_max_value_5_521):
													pass
												else:
													trap_x_max_value_6_522 = trap_x_max_value_5_521["page_info"]
													trap_x_max_index_7_523 = trap_x_min_index_7_509
													trap_x_max_value_7_524 = trap_x_max_value_6_522[trap_x_max_index_7_523]
													if not ("bounding_box" in trap_x_max_value_7_524):
														pass
													else:
														trap_x_max_value_8_525 = trap_x_max_value_7_524["bounding_box"]
														if not ("x_max" in trap_x_max_value_8_525):
															pass
														else:
															trap_x_max_value_9_526 = trap_x_max_value_8_525["x_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/x_max", trap_x_max_value_9_526, None)
										
										# Retrieve value of data property: trap_y_min
										trap_y_min_value_0_527 = resource_data_1["MineralSystem"]
										trap_y_min_index_1_528 = trap_x_min_index_1_494
										trap_y_min_value_1_529 = trap_y_min_value_0_527[trap_y_min_index_1_528]
										if not ("trap" in trap_y_min_value_1_529):
											pass
										else:
											trap_y_min_value_2_530 = trap_y_min_value_1_529["trap"]
											trap_y_min_index_3_531 = trap_x_min_index_3_499
											trap_y_min_value_3_532 = trap_y_min_value_2_530[trap_y_min_index_3_531]
											if not ("supporting_references" in trap_y_min_value_3_532):
												pass
											else:
												trap_y_min_value_4_533 = trap_y_min_value_3_532["supporting_references"]
												trap_y_min_index_5_534 = trap_x_min_index_5_504
												trap_y_min_value_5_535 = trap_y_min_value_4_533[trap_y_min_index_5_534]
												if not ("page_info" in trap_y_min_value_5_535):
													pass
												else:
													trap_y_min_value_6_536 = trap_y_min_value_5_535["page_info"]
													trap_y_min_index_7_537 = trap_x_min_index_7_509
													trap_y_min_value_7_538 = trap_y_min_value_6_536[trap_y_min_index_7_537]
													if not ("bounding_box" in trap_y_min_value_7_538):
														pass
													else:
														trap_y_min_value_8_539 = trap_y_min_value_7_538["bounding_box"]
														if not ("y_min" in trap_y_min_value_8_539):
															pass
														else:
															trap_y_min_value_9_540 = trap_y_min_value_8_539["y_min"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_min", trap_y_min_value_9_540, None)
										
										# Retrieve value of data property: trap_y_max
										trap_y_max_value_0_541 = resource_data_1["MineralSystem"]
										trap_y_max_index_1_542 = trap_x_min_index_1_494
										trap_y_max_value_1_543 = trap_y_max_value_0_541[trap_y_max_index_1_542]
										if not ("trap" in trap_y_max_value_1_543):
											pass
										else:
											trap_y_max_value_2_544 = trap_y_max_value_1_543["trap"]
											trap_y_max_index_3_545 = trap_x_min_index_3_499
											trap_y_max_value_3_546 = trap_y_max_value_2_544[trap_y_max_index_3_545]
											if not ("supporting_references" in trap_y_max_value_3_546):
												pass
											else:
												trap_y_max_value_4_547 = trap_y_max_value_3_546["supporting_references"]
												trap_y_max_index_5_548 = trap_x_min_index_5_504
												trap_y_max_value_5_549 = trap_y_max_value_4_547[trap_y_max_index_5_548]
												if not ("page_info" in trap_y_max_value_5_549):
													pass
												else:
													trap_y_max_value_6_550 = trap_y_max_value_5_549["page_info"]
													trap_y_max_index_7_551 = trap_x_min_index_7_509
													trap_y_max_value_7_552 = trap_y_max_value_6_550[trap_y_max_index_7_551]
													if not ("bounding_box" in trap_y_max_value_7_552):
														pass
													else:
														trap_y_max_value_8_553 = trap_y_max_value_7_552["bounding_box"]
														if not ("y_max" in trap_y_max_value_8_553):
															pass
														else:
															trap_y_max_value_9_554 = trap_y_max_value_8_553["y_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_max", trap_y_max_value_9_554, None)
										
										writer_2.end_record()
	
	# Transform records of class mndr:PageInfo:3
	trap_page_value_0_555 = resource_data_1["MineralSystem"]
	start_556 = 0
	end_557 = len(trap_page_value_0_555)
	for trap_page_index_1_558 in range(start_556, end_557):
		trap_page_value_1_559 = trap_page_value_0_555[trap_page_index_1_558]
		if not ("trap" in trap_page_value_1_559):
			continue
		else:
			trap_page_value_2_560 = trap_page_value_1_559["trap"]
			start_561 = 0
			end_562 = len(trap_page_value_2_560)
			for trap_page_index_3_563 in range(start_561, end_562):
				trap_page_value_3_564 = trap_page_value_2_560[trap_page_index_3_563]
				if not ("supporting_references" in trap_page_value_3_564):
					continue
				else:
					trap_page_value_4_565 = trap_page_value_3_564["supporting_references"]
					start_566 = 0
					end_567 = len(trap_page_value_4_565)
					for trap_page_index_5_568 in range(start_566, end_567):
						trap_page_value_5_569 = trap_page_value_4_565[trap_page_index_5_568]
						if not ("page_info" in trap_page_value_5_569):
							continue
						else:
							trap_page_value_6_570 = trap_page_value_5_569["page_info"]
							start_571 = 0
							end_572 = len(trap_page_value_6_570)
							for trap_page_index_7_573 in range(start_571, end_572):
								trap_page_value_7_574 = trap_page_value_6_570[trap_page_index_7_573]
								if not ("page" in trap_page_value_7_574):
									continue
								else:
									trap_page_value_8_575 = trap_page_value_7_574["page"]
									writer_2.begin_record("https://minmod.isi.edu/resource/PageInfo", (62, trap_page_index_1_558, trap_page_index_3_563, trap_page_index_5_568, trap_page_index_7_573), True, False)
									
									# Retrieve value of data property: trap_page
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/page", trap_page_value_8_575, None)
									
									# Retrieve value of object property: trap_x_min
									trap_x_min_value_0_576 = resource_data_1["MineralSystem"]
									trap_x_min_index_1_577 = trap_page_index_1_558
									trap_x_min_value_1_578 = trap_x_min_value_0_576[trap_x_min_index_1_577]
									if not ("trap" in trap_x_min_value_1_578):
										pass
									else:
										trap_x_min_value_2_579 = trap_x_min_value_1_578["trap"]
										trap_x_min_index_3_580 = trap_page_index_3_563
										trap_x_min_value_3_581 = trap_x_min_value_2_579[trap_x_min_index_3_580]
										if not ("supporting_references" in trap_x_min_value_3_581):
											pass
										else:
											trap_x_min_value_4_582 = trap_x_min_value_3_581["supporting_references"]
											trap_x_min_index_5_583 = trap_page_index_5_568
											trap_x_min_value_5_584 = trap_x_min_value_4_582[trap_x_min_index_5_583]
											if not ("page_info" in trap_x_min_value_5_584):
												pass
											else:
												trap_x_min_value_6_585 = trap_x_min_value_5_584["page_info"]
												trap_x_min_index_7_586 = trap_page_index_7_573
												trap_x_min_value_7_587 = trap_x_min_value_6_585[trap_x_min_index_7_586]
												if not ("bounding_box" in trap_x_min_value_7_587):
													pass
												else:
													trap_x_min_value_8_588 = trap_x_min_value_7_587["bounding_box"]
													if not ("x_min" in trap_x_min_value_8_588):
														pass
													else:
														trap_x_min_value_9_589 = trap_x_min_value_8_588["x_min"]
														if writer_2.has_written_record((64, trap_x_min_index_1_577, trap_x_min_index_3_580, trap_x_min_index_5_583, trap_x_min_index_7_586)):
															writer_2.write_object_property("https://minmod.isi.edu/resource/bounding_box", (64, trap_x_min_index_1_577, trap_x_min_index_3_580, trap_x_min_index_5_583, trap_x_min_index_7_586), True, True, False)
									
									writer_2.end_record()
	
	# Transform records of class mndr:Reference:3
	trap_id_document_value_0_590 = resource_data_1["MineralSystem"]
	start_591 = 0
	end_592 = len(trap_id_document_value_0_590)
	for trap_id_document_index_1_593 in range(start_591, end_592):
		trap_id_document_value_1_594 = trap_id_document_value_0_590[trap_id_document_index_1_593]
		if not ("trap" in trap_id_document_value_1_594):
			continue
		else:
			trap_id_document_value_2_595 = trap_id_document_value_1_594["trap"]
			start_596 = 0
			end_597 = len(trap_id_document_value_2_595)
			for trap_id_document_index_3_598 in range(start_596, end_597):
				trap_id_document_value_3_599 = trap_id_document_value_2_595[trap_id_document_index_3_598]
				if not ("supporting_references" in trap_id_document_value_3_599):
					continue
				else:
					trap_id_document_value_4_600 = trap_id_document_value_3_599["supporting_references"]
					start_601 = 0
					end_602 = len(trap_id_document_value_4_600)
					for trap_id_document_index_5_603 in range(start_601, end_602):
						trap_id_document_value_5_604 = trap_id_document_value_4_600[trap_id_document_index_5_603]
						if not ("document" in trap_id_document_value_5_604):
							continue
						else:
							trap_id_document_value_6_605 = trap_id_document_value_5_604["document"]
							trap_id_document_value_7_606 = trap_id_document_value_6_605["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (52, trap_id_document_index_1_593, trap_id_document_index_3_598, trap_id_document_index_5_603), True, False)
							
							# Retrieve value of data property: trap_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/document_id", trap_id_document_value_7_606, None)
							
							# Retrieve value of object property: trap_id_document
							if writer_2.has_written_record(trap_id_document_value_7_606):
								writer_2.write_object_property("https://minmod.isi.edu/resource/document", trap_id_document_value_7_606, True, False, False)
							
							# Retrieve value of object property: trap_page
							trap_page_value_0_607 = resource_data_1["MineralSystem"]
							trap_page_index_1_608 = trap_id_document_index_1_593
							trap_page_value_1_609 = trap_page_value_0_607[trap_page_index_1_608]
							if not ("trap" in trap_page_value_1_609):
								pass
							else:
								trap_page_value_2_610 = trap_page_value_1_609["trap"]
								trap_page_index_3_611 = trap_id_document_index_3_598
								trap_page_value_3_612 = trap_page_value_2_610[trap_page_index_3_611]
								if not ("supporting_references" in trap_page_value_3_612):
									pass
								else:
									trap_page_value_4_613 = trap_page_value_3_612["supporting_references"]
									trap_page_index_5_614 = trap_id_document_index_5_603
									trap_page_value_5_615 = trap_page_value_4_613[trap_page_index_5_614]
									if not ("page_info" in trap_page_value_5_615):
										pass
									else:
										trap_page_value_6_616 = trap_page_value_5_615["page_info"]
										start_617 = 0
										end_618 = len(trap_page_value_6_616)
										for trap_page_index_7_619 in range(start_617, end_618):
											trap_page_value_7_620 = trap_page_value_6_616[trap_page_index_7_619]
											if not ("page" in trap_page_value_7_620):
												pass
											else:
												trap_page_value_8_621 = trap_page_value_7_620["page"]
												if writer_2.has_written_record((62, trap_page_index_1_608, trap_page_index_3_611, trap_page_index_5_614, trap_page_index_7_619)):
													writer_2.write_object_property("https://minmod.isi.edu/resource/page_info", (62, trap_page_index_1_608, trap_page_index_3_611, trap_page_index_5_614, trap_page_index_7_619), True, True, False)
							
							writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:3
	trap_criteria_value_0_622 = resource_data_1["MineralSystem"]
	start_623 = 0
	end_624 = len(trap_criteria_value_0_622)
	for trap_criteria_index_1_625 in range(start_623, end_624):
		trap_criteria_value_1_626 = trap_criteria_value_0_622[trap_criteria_index_1_625]
		if not ("trap" in trap_criteria_value_1_626):
			continue
		else:
			trap_criteria_value_2_627 = trap_criteria_value_1_626["trap"]
			start_628 = 0
			end_629 = len(trap_criteria_value_2_627)
			for trap_criteria_index_3_630 in range(start_628, end_629):
				trap_criteria_value_3_631 = trap_criteria_value_2_627[trap_criteria_index_3_630]
				trap_criteria_value_4_632 = trap_criteria_value_3_631["criteria"]
				writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (46, trap_criteria_index_1_625, trap_criteria_index_3_630), True, False)
				
				# Retrieve value of data property: trap_criteria
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", trap_criteria_value_4_632, None)
				
				# Retrieve value of data property: trap_theoretical
				trap_theoretical_value_0_633 = resource_data_1["MineralSystem"]
				trap_theoretical_index_1_634 = trap_criteria_index_1_625
				trap_theoretical_value_1_635 = trap_theoretical_value_0_633[trap_theoretical_index_1_634]
				if not ("trap" in trap_theoretical_value_1_635):
					pass
				else:
					trap_theoretical_value_2_636 = trap_theoretical_value_1_635["trap"]
					trap_theoretical_index_3_637 = trap_criteria_index_3_630
					trap_theoretical_value_3_638 = trap_theoretical_value_2_636[trap_theoretical_index_3_637]
					if not ("theoretical" in trap_theoretical_value_3_638):
						pass
					else:
						trap_theoretical_value_4_639 = trap_theoretical_value_3_638["theoretical"]
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/theoretical", trap_theoretical_value_4_639, None)
				
				# Retrieve value of object property: trap_potential_dataset_name
				trap_potential_dataset_name_value_0_640 = resource_data_1["MineralSystem"]
				trap_potential_dataset_name_index_1_641 = trap_criteria_index_1_625
				trap_potential_dataset_name_value_1_642 = trap_potential_dataset_name_value_0_640[trap_potential_dataset_name_index_1_641]
				if not ("trap" in trap_potential_dataset_name_value_1_642):
					pass
				else:
					trap_potential_dataset_name_value_2_643 = trap_potential_dataset_name_value_1_642["trap"]
					trap_potential_dataset_name_index_3_644 = trap_criteria_index_3_630
					trap_potential_dataset_name_value_3_645 = trap_potential_dataset_name_value_2_643[trap_potential_dataset_name_index_3_644]
					if not ("potential_dataset" in trap_potential_dataset_name_value_3_645):
						pass
					else:
						trap_potential_dataset_name_value_4_646 = trap_potential_dataset_name_value_3_645["potential_dataset"]
						start_647 = 0
						end_648 = len(trap_potential_dataset_name_value_4_646)
						for trap_potential_dataset_name_index_5_649 in range(start_647, end_648):
							trap_potential_dataset_name_value_5_650 = trap_potential_dataset_name_value_4_646[trap_potential_dataset_name_index_5_649]
							trap_potential_dataset_name_value_6_651 = trap_potential_dataset_name_value_5_650["name"]
							if writer_2.has_written_record((48, trap_potential_dataset_name_index_1_641, trap_potential_dataset_name_index_3_644, trap_potential_dataset_name_index_5_649)):
								writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (48, trap_potential_dataset_name_index_1_641, trap_potential_dataset_name_index_3_644, trap_potential_dataset_name_index_5_649), True, True, False)
				
				# Retrieve value of object property: trap_id_document
				trap_id_document_value_0_652 = resource_data_1["MineralSystem"]
				trap_id_document_index_1_653 = trap_criteria_index_1_625
				trap_id_document_value_1_654 = trap_id_document_value_0_652[trap_id_document_index_1_653]
				if not ("trap" in trap_id_document_value_1_654):
					pass
				else:
					trap_id_document_value_2_655 = trap_id_document_value_1_654["trap"]
					trap_id_document_index_3_656 = trap_criteria_index_3_630
					trap_id_document_value_3_657 = trap_id_document_value_2_655[trap_id_document_index_3_656]
					if not ("supporting_references" in trap_id_document_value_3_657):
						pass
					else:
						trap_id_document_value_4_658 = trap_id_document_value_3_657["supporting_references"]
						start_659 = 0
						end_660 = len(trap_id_document_value_4_658)
						for trap_id_document_index_5_661 in range(start_659, end_660):
							trap_id_document_value_5_662 = trap_id_document_value_4_658[trap_id_document_index_5_661]
							if not ("document" in trap_id_document_value_5_662):
								pass
							else:
								trap_id_document_value_6_663 = trap_id_document_value_5_662["document"]
								trap_id_document_value_7_664 = trap_id_document_value_6_663["id"]
								if writer_2.has_written_record((52, trap_id_document_index_1_653, trap_id_document_index_3_656, trap_id_document_index_5_661)):
									writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (52, trap_id_document_index_1_653, trap_id_document_index_3_656, trap_id_document_index_5_661), True, True, False)
				
				writer_2.end_record()
	
	# Transform records of class mndr:EvidenceLayer:1
	source_potential_dataset_name_value_0_665 = resource_data_1["MineralSystem"]
	start_666 = 0
	end_667 = len(source_potential_dataset_name_value_0_665)
	for source_potential_dataset_name_index_1_668 in range(start_666, end_667):
		source_potential_dataset_name_value_1_669 = source_potential_dataset_name_value_0_665[source_potential_dataset_name_index_1_668]
		source_potential_dataset_name_value_2_670 = source_potential_dataset_name_value_1_669["source"]
		start_671 = 0
		end_672 = len(source_potential_dataset_name_value_2_670)
		for source_potential_dataset_name_index_3_673 in range(start_671, end_672):
			source_potential_dataset_name_value_3_674 = source_potential_dataset_name_value_2_670[source_potential_dataset_name_index_3_673]
			if not ("potential_dataset" in source_potential_dataset_name_value_3_674):
				continue
			else:
				source_potential_dataset_name_value_4_675 = source_potential_dataset_name_value_3_674["potential_dataset"]
				start_676 = 0
				end_677 = len(source_potential_dataset_name_value_4_675)
				for source_potential_dataset_name_index_5_678 in range(start_676, end_677):
					source_potential_dataset_name_value_5_679 = source_potential_dataset_name_value_4_675[source_potential_dataset_name_index_5_678]
					source_potential_dataset_name_value_6_680 = source_potential_dataset_name_value_5_679["name"]
					writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (4, source_potential_dataset_name_index_1_668, source_potential_dataset_name_index_3_673, source_potential_dataset_name_index_5_678), True, False)
					
					# Retrieve value of data property: source_potential_dataset_name
					if True:
						writer_2.write_data_property("https://minmod.isi.edu/resource/name", source_potential_dataset_name_value_6_680, None)
					
					# Retrieve value of data property: source_potential_dataset_score
					source_potential_dataset_score_value_0_681 = resource_data_1["MineralSystem"]
					source_potential_dataset_score_index_1_682 = source_potential_dataset_name_index_1_668
					source_potential_dataset_score_value_1_683 = source_potential_dataset_score_value_0_681[source_potential_dataset_score_index_1_682]
					source_potential_dataset_score_value_2_684 = source_potential_dataset_score_value_1_683["source"]
					source_potential_dataset_score_index_3_685 = source_potential_dataset_name_index_3_673
					source_potential_dataset_score_value_3_686 = source_potential_dataset_score_value_2_684[source_potential_dataset_score_index_3_685]
					if not ("potential_dataset" in source_potential_dataset_score_value_3_686):
						pass
					else:
						source_potential_dataset_score_value_4_687 = source_potential_dataset_score_value_3_686["potential_dataset"]
						source_potential_dataset_score_index_5_688 = source_potential_dataset_name_index_5_678
						source_potential_dataset_score_value_5_689 = source_potential_dataset_score_value_4_687[source_potential_dataset_score_index_5_688]
						source_potential_dataset_score_value_6_690 = source_potential_dataset_score_value_5_689["relevance_score"]
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", source_potential_dataset_score_value_6_690, None)
					
					writer_2.end_record()
	
	# Transform records of class mndr:Document:1
	source_id_document_value_0_691 = resource_data_1["MineralSystem"]
	start_692 = 0
	end_693 = len(source_id_document_value_0_691)
	for source_id_document_index_1_694 in range(start_692, end_693):
		source_id_document_value_1_695 = source_id_document_value_0_691[source_id_document_index_1_694]
		source_id_document_value_2_696 = source_id_document_value_1_695["source"]
		start_697 = 0
		end_698 = len(source_id_document_value_2_696)
		for source_id_document_index_3_699 in range(start_697, end_698):
			source_id_document_value_3_700 = source_id_document_value_2_696[source_id_document_index_3_699]
			if not ("supporting_references" in source_id_document_value_3_700):
				continue
			else:
				source_id_document_value_4_701 = source_id_document_value_3_700["supporting_references"]
				start_702 = 0
				end_703 = len(source_id_document_value_4_701)
				for source_id_document_index_5_704 in range(start_702, end_703):
					source_id_document_value_5_705 = source_id_document_value_4_701[source_id_document_index_5_704]
					if not ("document" in source_id_document_value_5_705):
						continue
					else:
						source_id_document_value_6_706 = source_id_document_value_5_705["document"]
						source_id_document_value_7_707 = source_id_document_value_6_706["id"]
						writer_2.begin_record("https://minmod.isi.edu/resource/Document", source_id_document_value_7_707, False, False)
						
						# Retrieve value of data property: source_id_document
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/id", source_id_document_value_7_707, None)
						
						# Retrieve value of data property: source_uri_document
						source_uri_document_value_0_708 = resource_data_1["MineralSystem"]
						source_uri_document_index_1_709 = source_id_document_index_1_694
						source_uri_document_value_1_710 = source_uri_document_value_0_708[source_uri_document_index_1_709]
						source_uri_document_value_2_711 = source_uri_document_value_1_710["source"]
						source_uri_document_index_3_712 = source_id_document_index_3_699
						source_uri_document_value_3_713 = source_uri_document_value_2_711[source_uri_document_index_3_712]
						if not ("supporting_references" in source_uri_document_value_3_713):
							pass
						else:
							source_uri_document_value_4_714 = source_uri_document_value_3_713["supporting_references"]
							source_uri_document_index_5_715 = source_id_document_index_5_704
							source_uri_document_value_5_716 = source_uri_document_value_4_714[source_uri_document_index_5_715]
							if not ("document" in source_uri_document_value_5_716):
								pass
							else:
								source_uri_document_value_6_717 = source_uri_document_value_5_716["document"]
								if not ("uri" in source_uri_document_value_6_717):
									pass
								else:
									source_uri_document_value_7_718 = source_uri_document_value_6_717["uri"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/uri", source_uri_document_value_7_718, None)
						
						# Retrieve value of data property: source_doi
						source_doi_value_0_719 = resource_data_1["MineralSystem"]
						source_doi_index_1_720 = source_id_document_index_1_694
						source_doi_value_1_721 = source_doi_value_0_719[source_doi_index_1_720]
						source_doi_value_2_722 = source_doi_value_1_721["source"]
						source_doi_index_3_723 = source_id_document_index_3_699
						source_doi_value_3_724 = source_doi_value_2_722[source_doi_index_3_723]
						if not ("supporting_references" in source_doi_value_3_724):
							pass
						else:
							source_doi_value_4_725 = source_doi_value_3_724["supporting_references"]
							source_doi_index_5_726 = source_id_document_index_5_704
							source_doi_value_5_727 = source_doi_value_4_725[source_doi_index_5_726]
							if not ("document" in source_doi_value_5_727):
								pass
							else:
								source_doi_value_6_728 = source_doi_value_5_727["document"]
								if not ("doi" in source_doi_value_6_728):
									pass
								else:
									source_doi_value_7_729 = source_doi_value_6_728["doi"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/doi", source_doi_value_7_729, None)
						
						# Retrieve value of data property: source_journal
						source_journal_value_0_730 = resource_data_1["MineralSystem"]
						source_journal_index_1_731 = source_id_document_index_1_694
						source_journal_value_1_732 = source_journal_value_0_730[source_journal_index_1_731]
						source_journal_value_2_733 = source_journal_value_1_732["source"]
						source_journal_index_3_734 = source_id_document_index_3_699
						source_journal_value_3_735 = source_journal_value_2_733[source_journal_index_3_734]
						if not ("supporting_references" in source_journal_value_3_735):
							pass
						else:
							source_journal_value_4_736 = source_journal_value_3_735["supporting_references"]
							source_journal_index_5_737 = source_id_document_index_5_704
							source_journal_value_5_738 = source_journal_value_4_736[source_journal_index_5_737]
							if not ("document" in source_journal_value_5_738):
								pass
							else:
								source_journal_value_6_739 = source_journal_value_5_738["document"]
								if not ("journal" in source_journal_value_6_739):
									pass
								else:
									source_journal_value_7_740 = source_journal_value_6_739["journal"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/journal", source_journal_value_7_740, None)
						
						# Retrieve value of data property: source_authors
						source_authors_value_0_741 = resource_data_1["MineralSystem"]
						source_authors_index_1_742 = source_id_document_index_1_694
						source_authors_value_1_743 = source_authors_value_0_741[source_authors_index_1_742]
						source_authors_value_2_744 = source_authors_value_1_743["source"]
						source_authors_index_3_745 = source_id_document_index_3_699
						source_authors_value_3_746 = source_authors_value_2_744[source_authors_index_3_745]
						if not ("supporting_references" in source_authors_value_3_746):
							pass
						else:
							source_authors_value_4_747 = source_authors_value_3_746["supporting_references"]
							source_authors_index_5_748 = source_id_document_index_5_704
							source_authors_value_5_749 = source_authors_value_4_747[source_authors_index_5_748]
							if not ("document" in source_authors_value_5_749):
								pass
							else:
								source_authors_value_6_750 = source_authors_value_5_749["document"]
								if not ("authors" in source_authors_value_6_750):
									pass
								else:
									source_authors_value_7_751 = source_authors_value_6_750["authors"]
									start_752 = 0
									end_753 = len(source_authors_value_7_751)
									for source_authors_index_8_754 in range(start_752, end_753):
										source_authors_value_8_755 = source_authors_value_7_751[source_authors_index_8_754]
										if True:
											writer_2.write_data_property("https://minmod.isi.edu/resource/authors", source_authors_value_8_755, None)
						
						# Retrieve value of data property: source_description_document
						source_description_document_value_0_756 = resource_data_1["MineralSystem"]
						source_description_document_index_1_757 = source_id_document_index_1_694
						source_description_document_value_1_758 = source_description_document_value_0_756[source_description_document_index_1_757]
						source_description_document_value_2_759 = source_description_document_value_1_758["source"]
						source_description_document_index_3_760 = source_id_document_index_3_699
						source_description_document_value_3_761 = source_description_document_value_2_759[source_description_document_index_3_760]
						if not ("supporting_references" in source_description_document_value_3_761):
							pass
						else:
							source_description_document_value_4_762 = source_description_document_value_3_761["supporting_references"]
							source_description_document_index_5_763 = source_id_document_index_5_704
							source_description_document_value_5_764 = source_description_document_value_4_762[source_description_document_index_5_763]
							if not ("document" in source_description_document_value_5_764):
								pass
							else:
								source_description_document_value_6_765 = source_description_document_value_5_764["document"]
								if not ("description" in source_description_document_value_6_765):
									pass
								else:
									source_description_document_value_7_766 = source_description_document_value_6_765["description"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/description", source_description_document_value_7_766, None)
						
						# Retrieve value of data property: source_title_document
						source_title_document_value_0_767 = resource_data_1["MineralSystem"]
						source_title_document_index_1_768 = source_id_document_index_1_694
						source_title_document_value_1_769 = source_title_document_value_0_767[source_title_document_index_1_768]
						source_title_document_value_2_770 = source_title_document_value_1_769["source"]
						source_title_document_index_3_771 = source_id_document_index_3_699
						source_title_document_value_3_772 = source_title_document_value_2_770[source_title_document_index_3_771]
						if not ("supporting_references" in source_title_document_value_3_772):
							pass
						else:
							source_title_document_value_4_773 = source_title_document_value_3_772["supporting_references"]
							source_title_document_index_5_774 = source_id_document_index_5_704
							source_title_document_value_5_775 = source_title_document_value_4_773[source_title_document_index_5_774]
							if not ("document" in source_title_document_value_5_775):
								pass
							else:
								source_title_document_value_6_776 = source_title_document_value_5_775["document"]
								if not ("title" in source_title_document_value_6_776):
									pass
								else:
									source_title_document_value_7_777 = source_title_document_value_6_776["title"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/title", source_title_document_value_7_777, None)
						
						# Retrieve value of data property: source_volume
						source_volume_value_0_778 = resource_data_1["MineralSystem"]
						source_volume_index_1_779 = source_id_document_index_1_694
						source_volume_value_1_780 = source_volume_value_0_778[source_volume_index_1_779]
						source_volume_value_2_781 = source_volume_value_1_780["source"]
						source_volume_index_3_782 = source_id_document_index_3_699
						source_volume_value_3_783 = source_volume_value_2_781[source_volume_index_3_782]
						if not ("supporting_references" in source_volume_value_3_783):
							pass
						else:
							source_volume_value_4_784 = source_volume_value_3_783["supporting_references"]
							source_volume_index_5_785 = source_id_document_index_5_704
							source_volume_value_5_786 = source_volume_value_4_784[source_volume_index_5_785]
							if not ("document" in source_volume_value_5_786):
								pass
							else:
								source_volume_value_6_787 = source_volume_value_5_786["document"]
								if not ("volume" in source_volume_value_6_787):
									pass
								else:
									source_volume_value_7_788 = source_volume_value_6_787["volume"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/volume", source_volume_value_7_788, None)
						
						# Retrieve value of data property: source_issue_document
						source_issue_document_value_0_789 = resource_data_1["MineralSystem"]
						source_issue_document_index_1_790 = source_id_document_index_1_694
						source_issue_document_value_1_791 = source_issue_document_value_0_789[source_issue_document_index_1_790]
						source_issue_document_value_2_792 = source_issue_document_value_1_791["source"]
						source_issue_document_index_3_793 = source_id_document_index_3_699
						source_issue_document_value_3_794 = source_issue_document_value_2_792[source_issue_document_index_3_793]
						if not ("supporting_references" in source_issue_document_value_3_794):
							pass
						else:
							source_issue_document_value_4_795 = source_issue_document_value_3_794["supporting_references"]
							source_issue_document_index_5_796 = source_id_document_index_5_704
							source_issue_document_value_5_797 = source_issue_document_value_4_795[source_issue_document_index_5_796]
							if not ("document" in source_issue_document_value_5_797):
								pass
							else:
								source_issue_document_value_6_798 = source_issue_document_value_5_797["document"]
								if not ("issue" in source_issue_document_value_6_798):
									pass
								else:
									source_issue_document_value_7_799 = source_issue_document_value_6_798["issue"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/issue", source_issue_document_value_7_799, None)
						
						# Retrieve value of data property: source_month_document
						source_month_document_value_0_800 = resource_data_1["MineralSystem"]
						source_month_document_index_1_801 = source_id_document_index_1_694
						source_month_document_value_1_802 = source_month_document_value_0_800[source_month_document_index_1_801]
						source_month_document_value_2_803 = source_month_document_value_1_802["source"]
						source_month_document_index_3_804 = source_id_document_index_3_699
						source_month_document_value_3_805 = source_month_document_value_2_803[source_month_document_index_3_804]
						if not ("supporting_references" in source_month_document_value_3_805):
							pass
						else:
							source_month_document_value_4_806 = source_month_document_value_3_805["supporting_references"]
							source_month_document_index_5_807 = source_id_document_index_5_704
							source_month_document_value_5_808 = source_month_document_value_4_806[source_month_document_index_5_807]
							if not ("document" in source_month_document_value_5_808):
								pass
							else:
								source_month_document_value_6_809 = source_month_document_value_5_808["document"]
								if not ("month" in source_month_document_value_6_809):
									pass
								else:
									source_month_document_value_7_810 = source_month_document_value_6_809["month"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/month", source_month_document_value_7_810, None)
						
						# Retrieve value of data property: source_year_document
						source_year_document_value_0_811 = resource_data_1["MineralSystem"]
						source_year_document_index_1_812 = source_id_document_index_1_694
						source_year_document_value_1_813 = source_year_document_value_0_811[source_year_document_index_1_812]
						source_year_document_value_2_814 = source_year_document_value_1_813["source"]
						source_year_document_index_3_815 = source_id_document_index_3_699
						source_year_document_value_3_816 = source_year_document_value_2_814[source_year_document_index_3_815]
						if not ("supporting_references" in source_year_document_value_3_816):
							pass
						else:
							source_year_document_value_4_817 = source_year_document_value_3_816["supporting_references"]
							source_year_document_index_5_818 = source_id_document_index_5_704
							source_year_document_value_5_819 = source_year_document_value_4_817[source_year_document_index_5_818]
							if not ("document" in source_year_document_value_5_819):
								pass
							else:
								source_year_document_value_6_820 = source_year_document_value_5_819["document"]
								if not ("year" in source_year_document_value_6_820):
									pass
								else:
									source_year_document_value_7_821 = source_year_document_value_6_820["year"]
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/year", source_year_document_value_7_821, None)
						
						writer_2.end_record()
	
	# Transform records of class mndr:BoundingBox:1
	source_x_min_value_0_822 = resource_data_1["MineralSystem"]
	start_823 = 0
	end_824 = len(source_x_min_value_0_822)
	for source_x_min_index_1_825 in range(start_823, end_824):
		source_x_min_value_1_826 = source_x_min_value_0_822[source_x_min_index_1_825]
		source_x_min_value_2_827 = source_x_min_value_1_826["source"]
		start_828 = 0
		end_829 = len(source_x_min_value_2_827)
		for source_x_min_index_3_830 in range(start_828, end_829):
			source_x_min_value_3_831 = source_x_min_value_2_827[source_x_min_index_3_830]
			if not ("supporting_references" in source_x_min_value_3_831):
				continue
			else:
				source_x_min_value_4_832 = source_x_min_value_3_831["supporting_references"]
				start_833 = 0
				end_834 = len(source_x_min_value_4_832)
				for source_x_min_index_5_835 in range(start_833, end_834):
					source_x_min_value_5_836 = source_x_min_value_4_832[source_x_min_index_5_835]
					if not ("page_info" in source_x_min_value_5_836):
						continue
					else:
						source_x_min_value_6_837 = source_x_min_value_5_836["page_info"]
						start_838 = 0
						end_839 = len(source_x_min_value_6_837)
						for source_x_min_index_7_840 in range(start_838, end_839):
							source_x_min_value_7_841 = source_x_min_value_6_837[source_x_min_index_7_840]
							if not ("bounding_box" in source_x_min_value_7_841):
								continue
							else:
								source_x_min_value_8_842 = source_x_min_value_7_841["bounding_box"]
								if not ("x_min" in source_x_min_value_8_842):
									continue
								else:
									source_x_min_value_9_843 = source_x_min_value_8_842["x_min"]
									writer_2.begin_record("https://minmod.isi.edu/resource/BoundingBox", (20, source_x_min_index_1_825, source_x_min_index_3_830, source_x_min_index_5_835, source_x_min_index_7_840), True, False)
									
									# Retrieve value of data property: source_x_min
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/x_min", source_x_min_value_9_843, None)
									
									# Retrieve value of data property: source_x_max
									source_x_max_value_0_844 = resource_data_1["MineralSystem"]
									source_x_max_index_1_845 = source_x_min_index_1_825
									source_x_max_value_1_846 = source_x_max_value_0_844[source_x_max_index_1_845]
									source_x_max_value_2_847 = source_x_max_value_1_846["source"]
									source_x_max_index_3_848 = source_x_min_index_3_830
									source_x_max_value_3_849 = source_x_max_value_2_847[source_x_max_index_3_848]
									if not ("supporting_references" in source_x_max_value_3_849):
										pass
									else:
										source_x_max_value_4_850 = source_x_max_value_3_849["supporting_references"]
										source_x_max_index_5_851 = source_x_min_index_5_835
										source_x_max_value_5_852 = source_x_max_value_4_850[source_x_max_index_5_851]
										if not ("page_info" in source_x_max_value_5_852):
											pass
										else:
											source_x_max_value_6_853 = source_x_max_value_5_852["page_info"]
											source_x_max_index_7_854 = source_x_min_index_7_840
											source_x_max_value_7_855 = source_x_max_value_6_853[source_x_max_index_7_854]
											if not ("bounding_box" in source_x_max_value_7_855):
												pass
											else:
												source_x_max_value_8_856 = source_x_max_value_7_855["bounding_box"]
												if not ("x_max" in source_x_max_value_8_856):
													pass
												else:
													source_x_max_value_9_857 = source_x_max_value_8_856["x_max"]
													if True:
														writer_2.write_data_property("https://minmod.isi.edu/resource/x_max", source_x_max_value_9_857, None)
									
									# Retrieve value of data property: source_y_min
									source_y_min_value_0_858 = resource_data_1["MineralSystem"]
									source_y_min_index_1_859 = source_x_min_index_1_825
									source_y_min_value_1_860 = source_y_min_value_0_858[source_y_min_index_1_859]
									source_y_min_value_2_861 = source_y_min_value_1_860["source"]
									source_y_min_index_3_862 = source_x_min_index_3_830
									source_y_min_value_3_863 = source_y_min_value_2_861[source_y_min_index_3_862]
									if not ("supporting_references" in source_y_min_value_3_863):
										pass
									else:
										source_y_min_value_4_864 = source_y_min_value_3_863["supporting_references"]
										source_y_min_index_5_865 = source_x_min_index_5_835
										source_y_min_value_5_866 = source_y_min_value_4_864[source_y_min_index_5_865]
										if not ("page_info" in source_y_min_value_5_866):
											pass
										else:
											source_y_min_value_6_867 = source_y_min_value_5_866["page_info"]
											source_y_min_index_7_868 = source_x_min_index_7_840
											source_y_min_value_7_869 = source_y_min_value_6_867[source_y_min_index_7_868]
											if not ("bounding_box" in source_y_min_value_7_869):
												pass
											else:
												source_y_min_value_8_870 = source_y_min_value_7_869["bounding_box"]
												if not ("y_min" in source_y_min_value_8_870):
													pass
												else:
													source_y_min_value_9_871 = source_y_min_value_8_870["y_min"]
													if True:
														writer_2.write_data_property("https://minmod.isi.edu/resource/y_min", source_y_min_value_9_871, None)
									
									# Retrieve value of data property: source_y_max
									source_y_max_value_0_872 = resource_data_1["MineralSystem"]
									source_y_max_index_1_873 = source_x_min_index_1_825
									source_y_max_value_1_874 = source_y_max_value_0_872[source_y_max_index_1_873]
									source_y_max_value_2_875 = source_y_max_value_1_874["source"]
									source_y_max_index_3_876 = source_x_min_index_3_830
									source_y_max_value_3_877 = source_y_max_value_2_875[source_y_max_index_3_876]
									if not ("supporting_references" in source_y_max_value_3_877):
										pass
									else:
										source_y_max_value_4_878 = source_y_max_value_3_877["supporting_references"]
										source_y_max_index_5_879 = source_x_min_index_5_835
										source_y_max_value_5_880 = source_y_max_value_4_878[source_y_max_index_5_879]
										if not ("page_info" in source_y_max_value_5_880):
											pass
										else:
											source_y_max_value_6_881 = source_y_max_value_5_880["page_info"]
											source_y_max_index_7_882 = source_x_min_index_7_840
											source_y_max_value_7_883 = source_y_max_value_6_881[source_y_max_index_7_882]
											if not ("bounding_box" in source_y_max_value_7_883):
												pass
											else:
												source_y_max_value_8_884 = source_y_max_value_7_883["bounding_box"]
												if not ("y_max" in source_y_max_value_8_884):
													pass
												else:
													source_y_max_value_9_885 = source_y_max_value_8_884["y_max"]
													if True:
														writer_2.write_data_property("https://minmod.isi.edu/resource/y_max", source_y_max_value_9_885, None)
									
									writer_2.end_record()
	
	# Transform records of class mndr:PageInfo:1
	source_page_value_0_886 = resource_data_1["MineralSystem"]
	start_887 = 0
	end_888 = len(source_page_value_0_886)
	for source_page_index_1_889 in range(start_887, end_888):
		source_page_value_1_890 = source_page_value_0_886[source_page_index_1_889]
		source_page_value_2_891 = source_page_value_1_890["source"]
		start_892 = 0
		end_893 = len(source_page_value_2_891)
		for source_page_index_3_894 in range(start_892, end_893):
			source_page_value_3_895 = source_page_value_2_891[source_page_index_3_894]
			if not ("supporting_references" in source_page_value_3_895):
				continue
			else:
				source_page_value_4_896 = source_page_value_3_895["supporting_references"]
				start_897 = 0
				end_898 = len(source_page_value_4_896)
				for source_page_index_5_899 in range(start_897, end_898):
					source_page_value_5_900 = source_page_value_4_896[source_page_index_5_899]
					if not ("page_info" in source_page_value_5_900):
						continue
					else:
						source_page_value_6_901 = source_page_value_5_900["page_info"]
						start_902 = 0
						end_903 = len(source_page_value_6_901)
						for source_page_index_7_904 in range(start_902, end_903):
							source_page_value_7_905 = source_page_value_6_901[source_page_index_7_904]
							if not ("page" in source_page_value_7_905):
								continue
							else:
								source_page_value_8_906 = source_page_value_7_905["page"]
								writer_2.begin_record("https://minmod.isi.edu/resource/PageInfo", (18, source_page_index_1_889, source_page_index_3_894, source_page_index_5_899, source_page_index_7_904), True, False)
								
								# Retrieve value of data property: source_page
								if True:
									writer_2.write_data_property("https://minmod.isi.edu/resource/page", source_page_value_8_906, None)
								
								# Retrieve value of object property: source_x_min
								source_x_min_value_0_907 = resource_data_1["MineralSystem"]
								source_x_min_index_1_908 = source_page_index_1_889
								source_x_min_value_1_909 = source_x_min_value_0_907[source_x_min_index_1_908]
								source_x_min_value_2_910 = source_x_min_value_1_909["source"]
								source_x_min_index_3_911 = source_page_index_3_894
								source_x_min_value_3_912 = source_x_min_value_2_910[source_x_min_index_3_911]
								if not ("supporting_references" in source_x_min_value_3_912):
									pass
								else:
									source_x_min_value_4_913 = source_x_min_value_3_912["supporting_references"]
									source_x_min_index_5_914 = source_page_index_5_899
									source_x_min_value_5_915 = source_x_min_value_4_913[source_x_min_index_5_914]
									if not ("page_info" in source_x_min_value_5_915):
										pass
									else:
										source_x_min_value_6_916 = source_x_min_value_5_915["page_info"]
										source_x_min_index_7_917 = source_page_index_7_904
										source_x_min_value_7_918 = source_x_min_value_6_916[source_x_min_index_7_917]
										if not ("bounding_box" in source_x_min_value_7_918):
											pass
										else:
											source_x_min_value_8_919 = source_x_min_value_7_918["bounding_box"]
											if not ("x_min" in source_x_min_value_8_919):
												pass
											else:
												source_x_min_value_9_920 = source_x_min_value_8_919["x_min"]
												if writer_2.has_written_record((20, source_x_min_index_1_908, source_x_min_index_3_911, source_x_min_index_5_914, source_x_min_index_7_917)):
													writer_2.write_object_property("https://minmod.isi.edu/resource/bounding_box", (20, source_x_min_index_1_908, source_x_min_index_3_911, source_x_min_index_5_914, source_x_min_index_7_917), True, True, False)
								
								writer_2.end_record()
	
	# Transform records of class mndr:Reference:1
	source_id_document_value_0_921 = resource_data_1["MineralSystem"]
	start_922 = 0
	end_923 = len(source_id_document_value_0_921)
	for source_id_document_index_1_924 in range(start_922, end_923):
		source_id_document_value_1_925 = source_id_document_value_0_921[source_id_document_index_1_924]
		source_id_document_value_2_926 = source_id_document_value_1_925["source"]
		start_927 = 0
		end_928 = len(source_id_document_value_2_926)
		for source_id_document_index_3_929 in range(start_927, end_928):
			source_id_document_value_3_930 = source_id_document_value_2_926[source_id_document_index_3_929]
			if not ("supporting_references" in source_id_document_value_3_930):
				continue
			else:
				source_id_document_value_4_931 = source_id_document_value_3_930["supporting_references"]
				start_932 = 0
				end_933 = len(source_id_document_value_4_931)
				for source_id_document_index_5_934 in range(start_932, end_933):
					source_id_document_value_5_935 = source_id_document_value_4_931[source_id_document_index_5_934]
					if not ("document" in source_id_document_value_5_935):
						continue
					else:
						source_id_document_value_6_936 = source_id_document_value_5_935["document"]
						source_id_document_value_7_937 = source_id_document_value_6_936["id"]
						writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (8, source_id_document_index_1_924, source_id_document_index_3_929, source_id_document_index_5_934), True, False)
						
						# Retrieve value of data property: source_id_document
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/document_id", source_id_document_value_7_937, None)
						
						# Retrieve value of object property: source_id_document
						if writer_2.has_written_record(source_id_document_value_7_937):
							writer_2.write_object_property("https://minmod.isi.edu/resource/document", source_id_document_value_7_937, True, False, False)
						
						# Retrieve value of object property: source_page
						source_page_value_0_938 = resource_data_1["MineralSystem"]
						source_page_index_1_939 = source_id_document_index_1_924
						source_page_value_1_940 = source_page_value_0_938[source_page_index_1_939]
						source_page_value_2_941 = source_page_value_1_940["source"]
						source_page_index_3_942 = source_id_document_index_3_929
						source_page_value_3_943 = source_page_value_2_941[source_page_index_3_942]
						if not ("supporting_references" in source_page_value_3_943):
							pass
						else:
							source_page_value_4_944 = source_page_value_3_943["supporting_references"]
							source_page_index_5_945 = source_id_document_index_5_934
							source_page_value_5_946 = source_page_value_4_944[source_page_index_5_945]
							if not ("page_info" in source_page_value_5_946):
								pass
							else:
								source_page_value_6_947 = source_page_value_5_946["page_info"]
								start_948 = 0
								end_949 = len(source_page_value_6_947)
								for source_page_index_7_950 in range(start_948, end_949):
									source_page_value_7_951 = source_page_value_6_947[source_page_index_7_950]
									if not ("page" in source_page_value_7_951):
										pass
									else:
										source_page_value_8_952 = source_page_value_7_951["page"]
										if writer_2.has_written_record((18, source_page_index_1_939, source_page_index_3_942, source_page_index_5_945, source_page_index_7_950)):
											writer_2.write_object_property("https://minmod.isi.edu/resource/page_info", (18, source_page_index_1_939, source_page_index_3_942, source_page_index_5_945, source_page_index_7_950), True, True, False)
						
						writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:1
	source_criteria_value_0_953 = resource_data_1["MineralSystem"]
	start_954 = 0
	end_955 = len(source_criteria_value_0_953)
	for source_criteria_index_1_956 in range(start_954, end_955):
		source_criteria_value_1_957 = source_criteria_value_0_953[source_criteria_index_1_956]
		source_criteria_value_2_958 = source_criteria_value_1_957["source"]
		start_959 = 0
		end_960 = len(source_criteria_value_2_958)
		for source_criteria_index_3_961 in range(start_959, end_960):
			source_criteria_value_3_962 = source_criteria_value_2_958[source_criteria_index_3_961]
			source_criteria_value_4_963 = source_criteria_value_3_962["criteria"]
			writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (2, source_criteria_index_1_956, source_criteria_index_3_961), True, False)
			
			# Retrieve value of data property: source_criteria
			writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", source_criteria_value_4_963, None)
			
			# Retrieve value of data property: source_theoretical
			source_theoretical_value_0_964 = resource_data_1["MineralSystem"]
			source_theoretical_index_1_965 = source_criteria_index_1_956
			source_theoretical_value_1_966 = source_theoretical_value_0_964[source_theoretical_index_1_965]
			source_theoretical_value_2_967 = source_theoretical_value_1_966["source"]
			source_theoretical_index_3_968 = source_criteria_index_3_961
			source_theoretical_value_3_969 = source_theoretical_value_2_967[source_theoretical_index_3_968]
			if not ("theoretical" in source_theoretical_value_3_969):
				pass
			else:
				source_theoretical_value_4_970 = source_theoretical_value_3_969["theoretical"]
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/theoretical", source_theoretical_value_4_970, None)
			
			# Retrieve value of object property: source_potential_dataset_name
			source_potential_dataset_name_value_0_971 = resource_data_1["MineralSystem"]
			source_potential_dataset_name_index_1_972 = source_criteria_index_1_956
			source_potential_dataset_name_value_1_973 = source_potential_dataset_name_value_0_971[source_potential_dataset_name_index_1_972]
			source_potential_dataset_name_value_2_974 = source_potential_dataset_name_value_1_973["source"]
			source_potential_dataset_name_index_3_975 = source_criteria_index_3_961
			source_potential_dataset_name_value_3_976 = source_potential_dataset_name_value_2_974[source_potential_dataset_name_index_3_975]
			if not ("potential_dataset" in source_potential_dataset_name_value_3_976):
				pass
			else:
				source_potential_dataset_name_value_4_977 = source_potential_dataset_name_value_3_976["potential_dataset"]
				start_978 = 0
				end_979 = len(source_potential_dataset_name_value_4_977)
				for source_potential_dataset_name_index_5_980 in range(start_978, end_979):
					source_potential_dataset_name_value_5_981 = source_potential_dataset_name_value_4_977[source_potential_dataset_name_index_5_980]
					source_potential_dataset_name_value_6_982 = source_potential_dataset_name_value_5_981["name"]
					if writer_2.has_written_record((4, source_potential_dataset_name_index_1_972, source_potential_dataset_name_index_3_975, source_potential_dataset_name_index_5_980)):
						writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (4, source_potential_dataset_name_index_1_972, source_potential_dataset_name_index_3_975, source_potential_dataset_name_index_5_980), True, True, False)
			
			# Retrieve value of object property: source_id_document
			source_id_document_value_0_983 = resource_data_1["MineralSystem"]
			source_id_document_index_1_984 = source_criteria_index_1_956
			source_id_document_value_1_985 = source_id_document_value_0_983[source_id_document_index_1_984]
			source_id_document_value_2_986 = source_id_document_value_1_985["source"]
			source_id_document_index_3_987 = source_criteria_index_3_961
			source_id_document_value_3_988 = source_id_document_value_2_986[source_id_document_index_3_987]
			if not ("supporting_references" in source_id_document_value_3_988):
				pass
			else:
				source_id_document_value_4_989 = source_id_document_value_3_988["supporting_references"]
				start_990 = 0
				end_991 = len(source_id_document_value_4_989)
				for source_id_document_index_5_992 in range(start_990, end_991):
					source_id_document_value_5_993 = source_id_document_value_4_989[source_id_document_index_5_992]
					if not ("document" in source_id_document_value_5_993):
						pass
					else:
						source_id_document_value_6_994 = source_id_document_value_5_993["document"]
						source_id_document_value_7_995 = source_id_document_value_6_994["id"]
						if writer_2.has_written_record((8, source_id_document_index_1_984, source_id_document_index_3_987, source_id_document_index_5_992)):
							writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (8, source_id_document_index_1_984, source_id_document_index_3_987, source_id_document_index_5_992), True, True, False)
			
			writer_2.end_record()
	
	# Transform records of class mndr:EvidenceLayer:4
	preservation_potential_dataset_name_value_0_996 = resource_data_1["MineralSystem"]
	start_997 = 0
	end_998 = len(preservation_potential_dataset_name_value_0_996)
	for preservation_potential_dataset_name_index_1_999 in range(start_997, end_998):
		preservation_potential_dataset_name_value_1_1000 = preservation_potential_dataset_name_value_0_996[preservation_potential_dataset_name_index_1_999]
		if not ("preservation" in preservation_potential_dataset_name_value_1_1000):
			continue
		else:
			preservation_potential_dataset_name_value_2_1001 = preservation_potential_dataset_name_value_1_1000["preservation"]
			start_1002 = 0
			end_1003 = len(preservation_potential_dataset_name_value_2_1001)
			for preservation_potential_dataset_name_index_3_1004 in range(start_1002, end_1003):
				preservation_potential_dataset_name_value_3_1005 = preservation_potential_dataset_name_value_2_1001[preservation_potential_dataset_name_index_3_1004]
				if not ("potential_dataset" in preservation_potential_dataset_name_value_3_1005):
					continue
				else:
					preservation_potential_dataset_name_value_4_1006 = preservation_potential_dataset_name_value_3_1005["potential_dataset"]
					start_1007 = 0
					end_1008 = len(preservation_potential_dataset_name_value_4_1006)
					for preservation_potential_dataset_name_index_5_1009 in range(start_1007, end_1008):
						preservation_potential_dataset_name_value_5_1010 = preservation_potential_dataset_name_value_4_1006[preservation_potential_dataset_name_index_5_1009]
						preservation_potential_dataset_name_value_6_1011 = preservation_potential_dataset_name_value_5_1010["name"]
						writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (70, preservation_potential_dataset_name_index_1_999, preservation_potential_dataset_name_index_3_1004, preservation_potential_dataset_name_index_5_1009), True, False)
						
						# Retrieve value of data property: preservation_potential_dataset_name
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/name", preservation_potential_dataset_name_value_6_1011, None)
						
						# Retrieve value of data property: preservation_potential_dataset_score
						preservation_potential_dataset_score_value_0_1012 = resource_data_1["MineralSystem"]
						preservation_potential_dataset_score_index_1_1013 = preservation_potential_dataset_name_index_1_999
						preservation_potential_dataset_score_value_1_1014 = preservation_potential_dataset_score_value_0_1012[preservation_potential_dataset_score_index_1_1013]
						if not ("preservation" in preservation_potential_dataset_score_value_1_1014):
							pass
						else:
							preservation_potential_dataset_score_value_2_1015 = preservation_potential_dataset_score_value_1_1014["preservation"]
							preservation_potential_dataset_score_index_3_1016 = preservation_potential_dataset_name_index_3_1004
							preservation_potential_dataset_score_value_3_1017 = preservation_potential_dataset_score_value_2_1015[preservation_potential_dataset_score_index_3_1016]
							if not ("potential_dataset" in preservation_potential_dataset_score_value_3_1017):
								pass
							else:
								preservation_potential_dataset_score_value_4_1018 = preservation_potential_dataset_score_value_3_1017["potential_dataset"]
								preservation_potential_dataset_score_index_5_1019 = preservation_potential_dataset_name_index_5_1009
								preservation_potential_dataset_score_value_5_1020 = preservation_potential_dataset_score_value_4_1018[preservation_potential_dataset_score_index_5_1019]
								preservation_potential_dataset_score_value_6_1021 = preservation_potential_dataset_score_value_5_1020["relevance_score"]
								if True:
									writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", preservation_potential_dataset_score_value_6_1021, None)
						
						writer_2.end_record()
	
	# Transform records of class mndr:Document:4
	preservation_id_document_value_0_1022 = resource_data_1["MineralSystem"]
	start_1023 = 0
	end_1024 = len(preservation_id_document_value_0_1022)
	for preservation_id_document_index_1_1025 in range(start_1023, end_1024):
		preservation_id_document_value_1_1026 = preservation_id_document_value_0_1022[preservation_id_document_index_1_1025]
		if not ("preservation" in preservation_id_document_value_1_1026):
			continue
		else:
			preservation_id_document_value_2_1027 = preservation_id_document_value_1_1026["preservation"]
			start_1028 = 0
			end_1029 = len(preservation_id_document_value_2_1027)
			for preservation_id_document_index_3_1030 in range(start_1028, end_1029):
				preservation_id_document_value_3_1031 = preservation_id_document_value_2_1027[preservation_id_document_index_3_1030]
				if not ("supporting_references" in preservation_id_document_value_3_1031):
					continue
				else:
					preservation_id_document_value_4_1032 = preservation_id_document_value_3_1031["supporting_references"]
					start_1033 = 0
					end_1034 = len(preservation_id_document_value_4_1032)
					for preservation_id_document_index_5_1035 in range(start_1033, end_1034):
						preservation_id_document_value_5_1036 = preservation_id_document_value_4_1032[preservation_id_document_index_5_1035]
						if not ("document" in preservation_id_document_value_5_1036):
							continue
						else:
							preservation_id_document_value_6_1037 = preservation_id_document_value_5_1036["document"]
							preservation_id_document_value_7_1038 = preservation_id_document_value_6_1037["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Document", preservation_id_document_value_7_1038, False, False)
							
							# Retrieve value of data property: preservation_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/id", preservation_id_document_value_7_1038, None)
							
							# Retrieve value of data property: preservation_uri_document
							preservation_uri_document_value_0_1039 = resource_data_1["MineralSystem"]
							preservation_uri_document_index_1_1040 = preservation_id_document_index_1_1025
							preservation_uri_document_value_1_1041 = preservation_uri_document_value_0_1039[preservation_uri_document_index_1_1040]
							if not ("preservation" in preservation_uri_document_value_1_1041):
								pass
							else:
								preservation_uri_document_value_2_1042 = preservation_uri_document_value_1_1041["preservation"]
								preservation_uri_document_index_3_1043 = preservation_id_document_index_3_1030
								preservation_uri_document_value_3_1044 = preservation_uri_document_value_2_1042[preservation_uri_document_index_3_1043]
								if not ("supporting_references" in preservation_uri_document_value_3_1044):
									pass
								else:
									preservation_uri_document_value_4_1045 = preservation_uri_document_value_3_1044["supporting_references"]
									preservation_uri_document_index_5_1046 = preservation_id_document_index_5_1035
									preservation_uri_document_value_5_1047 = preservation_uri_document_value_4_1045[preservation_uri_document_index_5_1046]
									if not ("document" in preservation_uri_document_value_5_1047):
										pass
									else:
										preservation_uri_document_value_6_1048 = preservation_uri_document_value_5_1047["document"]
										if not ("uri" in preservation_uri_document_value_6_1048):
											pass
										else:
											preservation_uri_document_value_7_1049 = preservation_uri_document_value_6_1048["uri"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/uri", preservation_uri_document_value_7_1049, None)
							
							# Retrieve value of data property: preservation_doi
							preservation_doi_value_0_1050 = resource_data_1["MineralSystem"]
							preservation_doi_index_1_1051 = preservation_id_document_index_1_1025
							preservation_doi_value_1_1052 = preservation_doi_value_0_1050[preservation_doi_index_1_1051]
							if not ("preservation" in preservation_doi_value_1_1052):
								pass
							else:
								preservation_doi_value_2_1053 = preservation_doi_value_1_1052["preservation"]
								preservation_doi_index_3_1054 = preservation_id_document_index_3_1030
								preservation_doi_value_3_1055 = preservation_doi_value_2_1053[preservation_doi_index_3_1054]
								if not ("supporting_references" in preservation_doi_value_3_1055):
									pass
								else:
									preservation_doi_value_4_1056 = preservation_doi_value_3_1055["supporting_references"]
									preservation_doi_index_5_1057 = preservation_id_document_index_5_1035
									preservation_doi_value_5_1058 = preservation_doi_value_4_1056[preservation_doi_index_5_1057]
									if not ("document" in preservation_doi_value_5_1058):
										pass
									else:
										preservation_doi_value_6_1059 = preservation_doi_value_5_1058["document"]
										if not ("doi" in preservation_doi_value_6_1059):
											pass
										else:
											preservation_doi_value_7_1060 = preservation_doi_value_6_1059["doi"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/doi", preservation_doi_value_7_1060, None)
							
							# Retrieve value of data property: preservation_journal
							preservation_journal_value_0_1061 = resource_data_1["MineralSystem"]
							preservation_journal_index_1_1062 = preservation_id_document_index_1_1025
							preservation_journal_value_1_1063 = preservation_journal_value_0_1061[preservation_journal_index_1_1062]
							if not ("preservation" in preservation_journal_value_1_1063):
								pass
							else:
								preservation_journal_value_2_1064 = preservation_journal_value_1_1063["preservation"]
								preservation_journal_index_3_1065 = preservation_id_document_index_3_1030
								preservation_journal_value_3_1066 = preservation_journal_value_2_1064[preservation_journal_index_3_1065]
								if not ("supporting_references" in preservation_journal_value_3_1066):
									pass
								else:
									preservation_journal_value_4_1067 = preservation_journal_value_3_1066["supporting_references"]
									preservation_journal_index_5_1068 = preservation_id_document_index_5_1035
									preservation_journal_value_5_1069 = preservation_journal_value_4_1067[preservation_journal_index_5_1068]
									if not ("document" in preservation_journal_value_5_1069):
										pass
									else:
										preservation_journal_value_6_1070 = preservation_journal_value_5_1069["document"]
										if not ("journal" in preservation_journal_value_6_1070):
											pass
										else:
											preservation_journal_value_7_1071 = preservation_journal_value_6_1070["journal"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/journal", preservation_journal_value_7_1071, None)
							
							# Retrieve value of data property: preservation_authors
							preservation_authors_value_0_1072 = resource_data_1["MineralSystem"]
							preservation_authors_index_1_1073 = preservation_id_document_index_1_1025
							preservation_authors_value_1_1074 = preservation_authors_value_0_1072[preservation_authors_index_1_1073]
							if not ("preservation" in preservation_authors_value_1_1074):
								pass
							else:
								preservation_authors_value_2_1075 = preservation_authors_value_1_1074["preservation"]
								preservation_authors_index_3_1076 = preservation_id_document_index_3_1030
								preservation_authors_value_3_1077 = preservation_authors_value_2_1075[preservation_authors_index_3_1076]
								if not ("supporting_references" in preservation_authors_value_3_1077):
									pass
								else:
									preservation_authors_value_4_1078 = preservation_authors_value_3_1077["supporting_references"]
									preservation_authors_index_5_1079 = preservation_id_document_index_5_1035
									preservation_authors_value_5_1080 = preservation_authors_value_4_1078[preservation_authors_index_5_1079]
									if not ("document" in preservation_authors_value_5_1080):
										pass
									else:
										preservation_authors_value_6_1081 = preservation_authors_value_5_1080["document"]
										if not ("authors" in preservation_authors_value_6_1081):
											pass
										else:
											preservation_authors_value_7_1082 = preservation_authors_value_6_1081["authors"]
											start_1083 = 0
											end_1084 = len(preservation_authors_value_7_1082)
											for preservation_authors_index_8_1085 in range(start_1083, end_1084):
												preservation_authors_value_8_1086 = preservation_authors_value_7_1082[preservation_authors_index_8_1085]
												if True:
													writer_2.write_data_property("https://minmod.isi.edu/resource/authors", preservation_authors_value_8_1086, None)
							
							# Retrieve value of data property: preservation_description_document
							preservation_description_document_value_0_1087 = resource_data_1["MineralSystem"]
							preservation_description_document_index_1_1088 = preservation_id_document_index_1_1025
							preservation_description_document_value_1_1089 = preservation_description_document_value_0_1087[preservation_description_document_index_1_1088]
							if not ("preservation" in preservation_description_document_value_1_1089):
								pass
							else:
								preservation_description_document_value_2_1090 = preservation_description_document_value_1_1089["preservation"]
								preservation_description_document_index_3_1091 = preservation_id_document_index_3_1030
								preservation_description_document_value_3_1092 = preservation_description_document_value_2_1090[preservation_description_document_index_3_1091]
								if not ("supporting_references" in preservation_description_document_value_3_1092):
									pass
								else:
									preservation_description_document_value_4_1093 = preservation_description_document_value_3_1092["supporting_references"]
									preservation_description_document_index_5_1094 = preservation_id_document_index_5_1035
									preservation_description_document_value_5_1095 = preservation_description_document_value_4_1093[preservation_description_document_index_5_1094]
									if not ("document" in preservation_description_document_value_5_1095):
										pass
									else:
										preservation_description_document_value_6_1096 = preservation_description_document_value_5_1095["document"]
										if not ("description" in preservation_description_document_value_6_1096):
											pass
										else:
											preservation_description_document_value_7_1097 = preservation_description_document_value_6_1096["description"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/description", preservation_description_document_value_7_1097, None)
							
							# Retrieve value of data property: preservation_title_document
							preservation_title_document_value_0_1098 = resource_data_1["MineralSystem"]
							preservation_title_document_index_1_1099 = preservation_id_document_index_1_1025
							preservation_title_document_value_1_1100 = preservation_title_document_value_0_1098[preservation_title_document_index_1_1099]
							if not ("preservation" in preservation_title_document_value_1_1100):
								pass
							else:
								preservation_title_document_value_2_1101 = preservation_title_document_value_1_1100["preservation"]
								preservation_title_document_index_3_1102 = preservation_id_document_index_3_1030
								preservation_title_document_value_3_1103 = preservation_title_document_value_2_1101[preservation_title_document_index_3_1102]
								if not ("supporting_references" in preservation_title_document_value_3_1103):
									pass
								else:
									preservation_title_document_value_4_1104 = preservation_title_document_value_3_1103["supporting_references"]
									preservation_title_document_index_5_1105 = preservation_id_document_index_5_1035
									preservation_title_document_value_5_1106 = preservation_title_document_value_4_1104[preservation_title_document_index_5_1105]
									if not ("document" in preservation_title_document_value_5_1106):
										pass
									else:
										preservation_title_document_value_6_1107 = preservation_title_document_value_5_1106["document"]
										if not ("title" in preservation_title_document_value_6_1107):
											pass
										else:
											preservation_title_document_value_7_1108 = preservation_title_document_value_6_1107["title"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/title", preservation_title_document_value_7_1108, None)
							
							# Retrieve value of data property: preservation_volume
							preservation_volume_value_0_1109 = resource_data_1["MineralSystem"]
							preservation_volume_index_1_1110 = preservation_id_document_index_1_1025
							preservation_volume_value_1_1111 = preservation_volume_value_0_1109[preservation_volume_index_1_1110]
							if not ("preservation" in preservation_volume_value_1_1111):
								pass
							else:
								preservation_volume_value_2_1112 = preservation_volume_value_1_1111["preservation"]
								preservation_volume_index_3_1113 = preservation_id_document_index_3_1030
								preservation_volume_value_3_1114 = preservation_volume_value_2_1112[preservation_volume_index_3_1113]
								if not ("supporting_references" in preservation_volume_value_3_1114):
									pass
								else:
									preservation_volume_value_4_1115 = preservation_volume_value_3_1114["supporting_references"]
									preservation_volume_index_5_1116 = preservation_id_document_index_5_1035
									preservation_volume_value_5_1117 = preservation_volume_value_4_1115[preservation_volume_index_5_1116]
									if not ("document" in preservation_volume_value_5_1117):
										pass
									else:
										preservation_volume_value_6_1118 = preservation_volume_value_5_1117["document"]
										if not ("volume" in preservation_volume_value_6_1118):
											pass
										else:
											preservation_volume_value_7_1119 = preservation_volume_value_6_1118["volume"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/volume", preservation_volume_value_7_1119, None)
							
							# Retrieve value of data property: preservation_issue_document
							preservation_issue_document_value_0_1120 = resource_data_1["MineralSystem"]
							preservation_issue_document_index_1_1121 = preservation_id_document_index_1_1025
							preservation_issue_document_value_1_1122 = preservation_issue_document_value_0_1120[preservation_issue_document_index_1_1121]
							if not ("preservation" in preservation_issue_document_value_1_1122):
								pass
							else:
								preservation_issue_document_value_2_1123 = preservation_issue_document_value_1_1122["preservation"]
								preservation_issue_document_index_3_1124 = preservation_id_document_index_3_1030
								preservation_issue_document_value_3_1125 = preservation_issue_document_value_2_1123[preservation_issue_document_index_3_1124]
								if not ("supporting_references" in preservation_issue_document_value_3_1125):
									pass
								else:
									preservation_issue_document_value_4_1126 = preservation_issue_document_value_3_1125["supporting_references"]
									preservation_issue_document_index_5_1127 = preservation_id_document_index_5_1035
									preservation_issue_document_value_5_1128 = preservation_issue_document_value_4_1126[preservation_issue_document_index_5_1127]
									if not ("document" in preservation_issue_document_value_5_1128):
										pass
									else:
										preservation_issue_document_value_6_1129 = preservation_issue_document_value_5_1128["document"]
										if not ("issue" in preservation_issue_document_value_6_1129):
											pass
										else:
											preservation_issue_document_value_7_1130 = preservation_issue_document_value_6_1129["issue"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/issue", preservation_issue_document_value_7_1130, None)
							
							# Retrieve value of data property: preservation_month_document
							preservation_month_document_value_0_1131 = resource_data_1["MineralSystem"]
							preservation_month_document_index_1_1132 = preservation_id_document_index_1_1025
							preservation_month_document_value_1_1133 = preservation_month_document_value_0_1131[preservation_month_document_index_1_1132]
							if not ("preservation" in preservation_month_document_value_1_1133):
								pass
							else:
								preservation_month_document_value_2_1134 = preservation_month_document_value_1_1133["preservation"]
								preservation_month_document_index_3_1135 = preservation_id_document_index_3_1030
								preservation_month_document_value_3_1136 = preservation_month_document_value_2_1134[preservation_month_document_index_3_1135]
								if not ("supporting_references" in preservation_month_document_value_3_1136):
									pass
								else:
									preservation_month_document_value_4_1137 = preservation_month_document_value_3_1136["supporting_references"]
									preservation_month_document_index_5_1138 = preservation_id_document_index_5_1035
									preservation_month_document_value_5_1139 = preservation_month_document_value_4_1137[preservation_month_document_index_5_1138]
									if not ("document" in preservation_month_document_value_5_1139):
										pass
									else:
										preservation_month_document_value_6_1140 = preservation_month_document_value_5_1139["document"]
										if not ("month" in preservation_month_document_value_6_1140):
											pass
										else:
											preservation_month_document_value_7_1141 = preservation_month_document_value_6_1140["month"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/month", preservation_month_document_value_7_1141, None)
							
							# Retrieve value of data property: preservation_year_document
							preservation_year_document_value_0_1142 = resource_data_1["MineralSystem"]
							preservation_year_document_index_1_1143 = preservation_id_document_index_1_1025
							preservation_year_document_value_1_1144 = preservation_year_document_value_0_1142[preservation_year_document_index_1_1143]
							if not ("preservation" in preservation_year_document_value_1_1144):
								pass
							else:
								preservation_year_document_value_2_1145 = preservation_year_document_value_1_1144["preservation"]
								preservation_year_document_index_3_1146 = preservation_id_document_index_3_1030
								preservation_year_document_value_3_1147 = preservation_year_document_value_2_1145[preservation_year_document_index_3_1146]
								if not ("supporting_references" in preservation_year_document_value_3_1147):
									pass
								else:
									preservation_year_document_value_4_1148 = preservation_year_document_value_3_1147["supporting_references"]
									preservation_year_document_index_5_1149 = preservation_id_document_index_5_1035
									preservation_year_document_value_5_1150 = preservation_year_document_value_4_1148[preservation_year_document_index_5_1149]
									if not ("document" in preservation_year_document_value_5_1150):
										pass
									else:
										preservation_year_document_value_6_1151 = preservation_year_document_value_5_1150["document"]
										if not ("year" in preservation_year_document_value_6_1151):
											pass
										else:
											preservation_year_document_value_7_1152 = preservation_year_document_value_6_1151["year"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/year", preservation_year_document_value_7_1152, None)
							
							writer_2.end_record()
	
	# Transform records of class mndr:BoundingBox:4
	preservation_x_min_value_0_1153 = resource_data_1["MineralSystem"]
	start_1154 = 0
	end_1155 = len(preservation_x_min_value_0_1153)
	for preservation_x_min_index_1_1156 in range(start_1154, end_1155):
		preservation_x_min_value_1_1157 = preservation_x_min_value_0_1153[preservation_x_min_index_1_1156]
		if not ("preservation" in preservation_x_min_value_1_1157):
			continue
		else:
			preservation_x_min_value_2_1158 = preservation_x_min_value_1_1157["preservation"]
			start_1159 = 0
			end_1160 = len(preservation_x_min_value_2_1158)
			for preservation_x_min_index_3_1161 in range(start_1159, end_1160):
				preservation_x_min_value_3_1162 = preservation_x_min_value_2_1158[preservation_x_min_index_3_1161]
				if not ("supporting_references" in preservation_x_min_value_3_1162):
					continue
				else:
					preservation_x_min_value_4_1163 = preservation_x_min_value_3_1162["supporting_references"]
					start_1164 = 0
					end_1165 = len(preservation_x_min_value_4_1163)
					for preservation_x_min_index_5_1166 in range(start_1164, end_1165):
						preservation_x_min_value_5_1167 = preservation_x_min_value_4_1163[preservation_x_min_index_5_1166]
						if not ("page_info" in preservation_x_min_value_5_1167):
							continue
						else:
							preservation_x_min_value_6_1168 = preservation_x_min_value_5_1167["page_info"]
							start_1169 = 0
							end_1170 = len(preservation_x_min_value_6_1168)
							for preservation_x_min_index_7_1171 in range(start_1169, end_1170):
								preservation_x_min_value_7_1172 = preservation_x_min_value_6_1168[preservation_x_min_index_7_1171]
								if not ("bounding_box" in preservation_x_min_value_7_1172):
									continue
								else:
									preservation_x_min_value_8_1173 = preservation_x_min_value_7_1172["bounding_box"]
									if not ("x_min" in preservation_x_min_value_8_1173):
										continue
									else:
										preservation_x_min_value_9_1174 = preservation_x_min_value_8_1173["x_min"]
										writer_2.begin_record("https://minmod.isi.edu/resource/BoundingBox", (86, preservation_x_min_index_1_1156, preservation_x_min_index_3_1161, preservation_x_min_index_5_1166, preservation_x_min_index_7_1171), True, False)
										
										# Retrieve value of data property: preservation_x_min
										if True:
											writer_2.write_data_property("https://minmod.isi.edu/resource/x_min", preservation_x_min_value_9_1174, None)
										
										# Retrieve value of data property: preservation_x_max
										preservation_x_max_value_0_1175 = resource_data_1["MineralSystem"]
										preservation_x_max_index_1_1176 = preservation_x_min_index_1_1156
										preservation_x_max_value_1_1177 = preservation_x_max_value_0_1175[preservation_x_max_index_1_1176]
										if not ("preservation" in preservation_x_max_value_1_1177):
											pass
										else:
											preservation_x_max_value_2_1178 = preservation_x_max_value_1_1177["preservation"]
											preservation_x_max_index_3_1179 = preservation_x_min_index_3_1161
											preservation_x_max_value_3_1180 = preservation_x_max_value_2_1178[preservation_x_max_index_3_1179]
											if not ("supporting_references" in preservation_x_max_value_3_1180):
												pass
											else:
												preservation_x_max_value_4_1181 = preservation_x_max_value_3_1180["supporting_references"]
												preservation_x_max_index_5_1182 = preservation_x_min_index_5_1166
												preservation_x_max_value_5_1183 = preservation_x_max_value_4_1181[preservation_x_max_index_5_1182]
												if not ("page_info" in preservation_x_max_value_5_1183):
													pass
												else:
													preservation_x_max_value_6_1184 = preservation_x_max_value_5_1183["page_info"]
													preservation_x_max_index_7_1185 = preservation_x_min_index_7_1171
													preservation_x_max_value_7_1186 = preservation_x_max_value_6_1184[preservation_x_max_index_7_1185]
													if not ("bounding_box" in preservation_x_max_value_7_1186):
														pass
													else:
														preservation_x_max_value_8_1187 = preservation_x_max_value_7_1186["bounding_box"]
														if not ("x_max" in preservation_x_max_value_8_1187):
															pass
														else:
															preservation_x_max_value_9_1188 = preservation_x_max_value_8_1187["x_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/x_max", preservation_x_max_value_9_1188, None)
										
										# Retrieve value of data property: preservation_y_min
										preservation_y_min_value_0_1189 = resource_data_1["MineralSystem"]
										preservation_y_min_index_1_1190 = preservation_x_min_index_1_1156
										preservation_y_min_value_1_1191 = preservation_y_min_value_0_1189[preservation_y_min_index_1_1190]
										if not ("preservation" in preservation_y_min_value_1_1191):
											pass
										else:
											preservation_y_min_value_2_1192 = preservation_y_min_value_1_1191["preservation"]
											preservation_y_min_index_3_1193 = preservation_x_min_index_3_1161
											preservation_y_min_value_3_1194 = preservation_y_min_value_2_1192[preservation_y_min_index_3_1193]
											if not ("supporting_references" in preservation_y_min_value_3_1194):
												pass
											else:
												preservation_y_min_value_4_1195 = preservation_y_min_value_3_1194["supporting_references"]
												preservation_y_min_index_5_1196 = preservation_x_min_index_5_1166
												preservation_y_min_value_5_1197 = preservation_y_min_value_4_1195[preservation_y_min_index_5_1196]
												if not ("page_info" in preservation_y_min_value_5_1197):
													pass
												else:
													preservation_y_min_value_6_1198 = preservation_y_min_value_5_1197["page_info"]
													preservation_y_min_index_7_1199 = preservation_x_min_index_7_1171
													preservation_y_min_value_7_1200 = preservation_y_min_value_6_1198[preservation_y_min_index_7_1199]
													if not ("bounding_box" in preservation_y_min_value_7_1200):
														pass
													else:
														preservation_y_min_value_8_1201 = preservation_y_min_value_7_1200["bounding_box"]
														if not ("y_min" in preservation_y_min_value_8_1201):
															pass
														else:
															preservation_y_min_value_9_1202 = preservation_y_min_value_8_1201["y_min"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_min", preservation_y_min_value_9_1202, None)
										
										# Retrieve value of data property: preservation_y_max
										preservation_y_max_value_0_1203 = resource_data_1["MineralSystem"]
										preservation_y_max_index_1_1204 = preservation_x_min_index_1_1156
										preservation_y_max_value_1_1205 = preservation_y_max_value_0_1203[preservation_y_max_index_1_1204]
										if not ("preservation" in preservation_y_max_value_1_1205):
											pass
										else:
											preservation_y_max_value_2_1206 = preservation_y_max_value_1_1205["preservation"]
											preservation_y_max_index_3_1207 = preservation_x_min_index_3_1161
											preservation_y_max_value_3_1208 = preservation_y_max_value_2_1206[preservation_y_max_index_3_1207]
											if not ("supporting_references" in preservation_y_max_value_3_1208):
												pass
											else:
												preservation_y_max_value_4_1209 = preservation_y_max_value_3_1208["supporting_references"]
												preservation_y_max_index_5_1210 = preservation_x_min_index_5_1166
												preservation_y_max_value_5_1211 = preservation_y_max_value_4_1209[preservation_y_max_index_5_1210]
												if not ("page_info" in preservation_y_max_value_5_1211):
													pass
												else:
													preservation_y_max_value_6_1212 = preservation_y_max_value_5_1211["page_info"]
													preservation_y_max_index_7_1213 = preservation_x_min_index_7_1171
													preservation_y_max_value_7_1214 = preservation_y_max_value_6_1212[preservation_y_max_index_7_1213]
													if not ("bounding_box" in preservation_y_max_value_7_1214):
														pass
													else:
														preservation_y_max_value_8_1215 = preservation_y_max_value_7_1214["bounding_box"]
														if not ("y_max" in preservation_y_max_value_8_1215):
															pass
														else:
															preservation_y_max_value_9_1216 = preservation_y_max_value_8_1215["y_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_max", preservation_y_max_value_9_1216, None)
										
										writer_2.end_record()
	
	# Transform records of class mndr:PageInfo:4
	preservation_page_value_0_1217 = resource_data_1["MineralSystem"]
	start_1218 = 0
	end_1219 = len(preservation_page_value_0_1217)
	for preservation_page_index_1_1220 in range(start_1218, end_1219):
		preservation_page_value_1_1221 = preservation_page_value_0_1217[preservation_page_index_1_1220]
		if not ("preservation" in preservation_page_value_1_1221):
			continue
		else:
			preservation_page_value_2_1222 = preservation_page_value_1_1221["preservation"]
			start_1223 = 0
			end_1224 = len(preservation_page_value_2_1222)
			for preservation_page_index_3_1225 in range(start_1223, end_1224):
				preservation_page_value_3_1226 = preservation_page_value_2_1222[preservation_page_index_3_1225]
				if not ("supporting_references" in preservation_page_value_3_1226):
					continue
				else:
					preservation_page_value_4_1227 = preservation_page_value_3_1226["supporting_references"]
					start_1228 = 0
					end_1229 = len(preservation_page_value_4_1227)
					for preservation_page_index_5_1230 in range(start_1228, end_1229):
						preservation_page_value_5_1231 = preservation_page_value_4_1227[preservation_page_index_5_1230]
						if not ("page_info" in preservation_page_value_5_1231):
							continue
						else:
							preservation_page_value_6_1232 = preservation_page_value_5_1231["page_info"]
							start_1233 = 0
							end_1234 = len(preservation_page_value_6_1232)
							for preservation_page_index_7_1235 in range(start_1233, end_1234):
								preservation_page_value_7_1236 = preservation_page_value_6_1232[preservation_page_index_7_1235]
								if not ("page" in preservation_page_value_7_1236):
									continue
								else:
									preservation_page_value_8_1237 = preservation_page_value_7_1236["page"]
									writer_2.begin_record("https://minmod.isi.edu/resource/PageInfo", (84, preservation_page_index_1_1220, preservation_page_index_3_1225, preservation_page_index_5_1230, preservation_page_index_7_1235), True, False)
									
									# Retrieve value of data property: preservation_page
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/page", preservation_page_value_8_1237, None)
									
									# Retrieve value of object property: preservation_x_min
									preservation_x_min_value_0_1238 = resource_data_1["MineralSystem"]
									preservation_x_min_index_1_1239 = preservation_page_index_1_1220
									preservation_x_min_value_1_1240 = preservation_x_min_value_0_1238[preservation_x_min_index_1_1239]
									if not ("preservation" in preservation_x_min_value_1_1240):
										pass
									else:
										preservation_x_min_value_2_1241 = preservation_x_min_value_1_1240["preservation"]
										preservation_x_min_index_3_1242 = preservation_page_index_3_1225
										preservation_x_min_value_3_1243 = preservation_x_min_value_2_1241[preservation_x_min_index_3_1242]
										if not ("supporting_references" in preservation_x_min_value_3_1243):
											pass
										else:
											preservation_x_min_value_4_1244 = preservation_x_min_value_3_1243["supporting_references"]
											preservation_x_min_index_5_1245 = preservation_page_index_5_1230
											preservation_x_min_value_5_1246 = preservation_x_min_value_4_1244[preservation_x_min_index_5_1245]
											if not ("page_info" in preservation_x_min_value_5_1246):
												pass
											else:
												preservation_x_min_value_6_1247 = preservation_x_min_value_5_1246["page_info"]
												preservation_x_min_index_7_1248 = preservation_page_index_7_1235
												preservation_x_min_value_7_1249 = preservation_x_min_value_6_1247[preservation_x_min_index_7_1248]
												if not ("bounding_box" in preservation_x_min_value_7_1249):
													pass
												else:
													preservation_x_min_value_8_1250 = preservation_x_min_value_7_1249["bounding_box"]
													if not ("x_min" in preservation_x_min_value_8_1250):
														pass
													else:
														preservation_x_min_value_9_1251 = preservation_x_min_value_8_1250["x_min"]
														if writer_2.has_written_record((86, preservation_x_min_index_1_1239, preservation_x_min_index_3_1242, preservation_x_min_index_5_1245, preservation_x_min_index_7_1248)):
															writer_2.write_object_property("https://minmod.isi.edu/resource/bounding_box", (86, preservation_x_min_index_1_1239, preservation_x_min_index_3_1242, preservation_x_min_index_5_1245, preservation_x_min_index_7_1248), True, True, False)
									
									writer_2.end_record()
	
	# Transform records of class mndr:Reference:4
	preservation_id_document_value_0_1252 = resource_data_1["MineralSystem"]
	start_1253 = 0
	end_1254 = len(preservation_id_document_value_0_1252)
	for preservation_id_document_index_1_1255 in range(start_1253, end_1254):
		preservation_id_document_value_1_1256 = preservation_id_document_value_0_1252[preservation_id_document_index_1_1255]
		if not ("preservation" in preservation_id_document_value_1_1256):
			continue
		else:
			preservation_id_document_value_2_1257 = preservation_id_document_value_1_1256["preservation"]
			start_1258 = 0
			end_1259 = len(preservation_id_document_value_2_1257)
			for preservation_id_document_index_3_1260 in range(start_1258, end_1259):
				preservation_id_document_value_3_1261 = preservation_id_document_value_2_1257[preservation_id_document_index_3_1260]
				if not ("supporting_references" in preservation_id_document_value_3_1261):
					continue
				else:
					preservation_id_document_value_4_1262 = preservation_id_document_value_3_1261["supporting_references"]
					start_1263 = 0
					end_1264 = len(preservation_id_document_value_4_1262)
					for preservation_id_document_index_5_1265 in range(start_1263, end_1264):
						preservation_id_document_value_5_1266 = preservation_id_document_value_4_1262[preservation_id_document_index_5_1265]
						if not ("document" in preservation_id_document_value_5_1266):
							continue
						else:
							preservation_id_document_value_6_1267 = preservation_id_document_value_5_1266["document"]
							preservation_id_document_value_7_1268 = preservation_id_document_value_6_1267["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (74, preservation_id_document_index_1_1255, preservation_id_document_index_3_1260, preservation_id_document_index_5_1265), True, False)
							
							# Retrieve value of data property: preservation_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/document_id", preservation_id_document_value_7_1268, None)
							
							# Retrieve value of object property: preservation_id_document
							if writer_2.has_written_record(preservation_id_document_value_7_1268):
								writer_2.write_object_property("https://minmod.isi.edu/resource/document", preservation_id_document_value_7_1268, True, False, False)
							
							# Retrieve value of object property: preservation_page
							preservation_page_value_0_1269 = resource_data_1["MineralSystem"]
							preservation_page_index_1_1270 = preservation_id_document_index_1_1255
							preservation_page_value_1_1271 = preservation_page_value_0_1269[preservation_page_index_1_1270]
							if not ("preservation" in preservation_page_value_1_1271):
								pass
							else:
								preservation_page_value_2_1272 = preservation_page_value_1_1271["preservation"]
								preservation_page_index_3_1273 = preservation_id_document_index_3_1260
								preservation_page_value_3_1274 = preservation_page_value_2_1272[preservation_page_index_3_1273]
								if not ("supporting_references" in preservation_page_value_3_1274):
									pass
								else:
									preservation_page_value_4_1275 = preservation_page_value_3_1274["supporting_references"]
									preservation_page_index_5_1276 = preservation_id_document_index_5_1265
									preservation_page_value_5_1277 = preservation_page_value_4_1275[preservation_page_index_5_1276]
									if not ("page_info" in preservation_page_value_5_1277):
										pass
									else:
										preservation_page_value_6_1278 = preservation_page_value_5_1277["page_info"]
										start_1279 = 0
										end_1280 = len(preservation_page_value_6_1278)
										for preservation_page_index_7_1281 in range(start_1279, end_1280):
											preservation_page_value_7_1282 = preservation_page_value_6_1278[preservation_page_index_7_1281]
											if not ("page" in preservation_page_value_7_1282):
												pass
											else:
												preservation_page_value_8_1283 = preservation_page_value_7_1282["page"]
												if writer_2.has_written_record((84, preservation_page_index_1_1270, preservation_page_index_3_1273, preservation_page_index_5_1276, preservation_page_index_7_1281)):
													writer_2.write_object_property("https://minmod.isi.edu/resource/page_info", (84, preservation_page_index_1_1270, preservation_page_index_3_1273, preservation_page_index_5_1276, preservation_page_index_7_1281), True, True, False)
							
							writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:4
	preservation_criteria_value_0_1284 = resource_data_1["MineralSystem"]
	start_1285 = 0
	end_1286 = len(preservation_criteria_value_0_1284)
	for preservation_criteria_index_1_1287 in range(start_1285, end_1286):
		preservation_criteria_value_1_1288 = preservation_criteria_value_0_1284[preservation_criteria_index_1_1287]
		if not ("preservation" in preservation_criteria_value_1_1288):
			continue
		else:
			preservation_criteria_value_2_1289 = preservation_criteria_value_1_1288["preservation"]
			start_1290 = 0
			end_1291 = len(preservation_criteria_value_2_1289)
			for preservation_criteria_index_3_1292 in range(start_1290, end_1291):
				preservation_criteria_value_3_1293 = preservation_criteria_value_2_1289[preservation_criteria_index_3_1292]
				preservation_criteria_value_4_1294 = preservation_criteria_value_3_1293["criteria"]
				writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (68, preservation_criteria_index_1_1287, preservation_criteria_index_3_1292), True, False)
				
				# Retrieve value of data property: preservation_criteria
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", preservation_criteria_value_4_1294, None)
				
				# Retrieve value of data property: preservation_theoretical
				preservation_theoretical_value_0_1295 = resource_data_1["MineralSystem"]
				preservation_theoretical_index_1_1296 = preservation_criteria_index_1_1287
				preservation_theoretical_value_1_1297 = preservation_theoretical_value_0_1295[preservation_theoretical_index_1_1296]
				if not ("preservation" in preservation_theoretical_value_1_1297):
					pass
				else:
					preservation_theoretical_value_2_1298 = preservation_theoretical_value_1_1297["preservation"]
					preservation_theoretical_index_3_1299 = preservation_criteria_index_3_1292
					preservation_theoretical_value_3_1300 = preservation_theoretical_value_2_1298[preservation_theoretical_index_3_1299]
					if not ("theoretical" in preservation_theoretical_value_3_1300):
						pass
					else:
						preservation_theoretical_value_4_1301 = preservation_theoretical_value_3_1300["theoretical"]
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/theoretical", preservation_theoretical_value_4_1301, None)
				
				# Retrieve value of object property: preservation_potential_dataset_name
				preservation_potential_dataset_name_value_0_1302 = resource_data_1["MineralSystem"]
				preservation_potential_dataset_name_index_1_1303 = preservation_criteria_index_1_1287
				preservation_potential_dataset_name_value_1_1304 = preservation_potential_dataset_name_value_0_1302[preservation_potential_dataset_name_index_1_1303]
				if not ("preservation" in preservation_potential_dataset_name_value_1_1304):
					pass
				else:
					preservation_potential_dataset_name_value_2_1305 = preservation_potential_dataset_name_value_1_1304["preservation"]
					preservation_potential_dataset_name_index_3_1306 = preservation_criteria_index_3_1292
					preservation_potential_dataset_name_value_3_1307 = preservation_potential_dataset_name_value_2_1305[preservation_potential_dataset_name_index_3_1306]
					if not ("potential_dataset" in preservation_potential_dataset_name_value_3_1307):
						pass
					else:
						preservation_potential_dataset_name_value_4_1308 = preservation_potential_dataset_name_value_3_1307["potential_dataset"]
						start_1309 = 0
						end_1310 = len(preservation_potential_dataset_name_value_4_1308)
						for preservation_potential_dataset_name_index_5_1311 in range(start_1309, end_1310):
							preservation_potential_dataset_name_value_5_1312 = preservation_potential_dataset_name_value_4_1308[preservation_potential_dataset_name_index_5_1311]
							preservation_potential_dataset_name_value_6_1313 = preservation_potential_dataset_name_value_5_1312["name"]
							if writer_2.has_written_record((70, preservation_potential_dataset_name_index_1_1303, preservation_potential_dataset_name_index_3_1306, preservation_potential_dataset_name_index_5_1311)):
								writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (70, preservation_potential_dataset_name_index_1_1303, preservation_potential_dataset_name_index_3_1306, preservation_potential_dataset_name_index_5_1311), True, True, False)
				
				# Retrieve value of object property: preservation_id_document
				preservation_id_document_value_0_1314 = resource_data_1["MineralSystem"]
				preservation_id_document_index_1_1315 = preservation_criteria_index_1_1287
				preservation_id_document_value_1_1316 = preservation_id_document_value_0_1314[preservation_id_document_index_1_1315]
				if not ("preservation" in preservation_id_document_value_1_1316):
					pass
				else:
					preservation_id_document_value_2_1317 = preservation_id_document_value_1_1316["preservation"]
					preservation_id_document_index_3_1318 = preservation_criteria_index_3_1292
					preservation_id_document_value_3_1319 = preservation_id_document_value_2_1317[preservation_id_document_index_3_1318]
					if not ("supporting_references" in preservation_id_document_value_3_1319):
						pass
					else:
						preservation_id_document_value_4_1320 = preservation_id_document_value_3_1319["supporting_references"]
						start_1321 = 0
						end_1322 = len(preservation_id_document_value_4_1320)
						for preservation_id_document_index_5_1323 in range(start_1321, end_1322):
							preservation_id_document_value_5_1324 = preservation_id_document_value_4_1320[preservation_id_document_index_5_1323]
							if not ("document" in preservation_id_document_value_5_1324):
								pass
							else:
								preservation_id_document_value_6_1325 = preservation_id_document_value_5_1324["document"]
								preservation_id_document_value_7_1326 = preservation_id_document_value_6_1325["id"]
								if writer_2.has_written_record((74, preservation_id_document_index_1_1315, preservation_id_document_index_3_1318, preservation_id_document_index_5_1323)):
									writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (74, preservation_id_document_index_1_1315, preservation_id_document_index_3_1318, preservation_id_document_index_5_1323), True, True, False)
				
				writer_2.end_record()
	
	# Transform records of class mndr:EvidenceLayer:6
	outflow_potential_dataset_name_value_0_1327 = resource_data_1["MineralSystem"]
	start_1328 = 0
	end_1329 = len(outflow_potential_dataset_name_value_0_1327)
	for outflow_potential_dataset_name_index_1_1330 in range(start_1328, end_1329):
		outflow_potential_dataset_name_value_1_1331 = outflow_potential_dataset_name_value_0_1327[outflow_potential_dataset_name_index_1_1330]
		if not ("outflow" in outflow_potential_dataset_name_value_1_1331):
			continue
		else:
			outflow_potential_dataset_name_value_2_1332 = outflow_potential_dataset_name_value_1_1331["outflow"]
			start_1333 = 0
			end_1334 = len(outflow_potential_dataset_name_value_2_1332)
			for outflow_potential_dataset_name_index_3_1335 in range(start_1333, end_1334):
				outflow_potential_dataset_name_value_3_1336 = outflow_potential_dataset_name_value_2_1332[outflow_potential_dataset_name_index_3_1335]
				if not ("potential_dataset" in outflow_potential_dataset_name_value_3_1336):
					continue
				else:
					outflow_potential_dataset_name_value_4_1337 = outflow_potential_dataset_name_value_3_1336["potential_dataset"]
					start_1338 = 0
					end_1339 = len(outflow_potential_dataset_name_value_4_1337)
					for outflow_potential_dataset_name_index_5_1340 in range(start_1338, end_1339):
						outflow_potential_dataset_name_value_5_1341 = outflow_potential_dataset_name_value_4_1337[outflow_potential_dataset_name_index_5_1340]
						outflow_potential_dataset_name_value_6_1342 = outflow_potential_dataset_name_value_5_1341["name"]
						writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (114, outflow_potential_dataset_name_index_1_1330, outflow_potential_dataset_name_index_3_1335, outflow_potential_dataset_name_index_5_1340), True, False)
						
						# Retrieve value of data property: outflow_potential_dataset_name
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/name", outflow_potential_dataset_name_value_6_1342, None)
						
						# Retrieve value of data property: outflow_potential_dataset_score
						outflow_potential_dataset_score_value_0_1343 = resource_data_1["MineralSystem"]
						outflow_potential_dataset_score_index_1_1344 = outflow_potential_dataset_name_index_1_1330
						outflow_potential_dataset_score_value_1_1345 = outflow_potential_dataset_score_value_0_1343[outflow_potential_dataset_score_index_1_1344]
						if not ("outflow" in outflow_potential_dataset_score_value_1_1345):
							pass
						else:
							outflow_potential_dataset_score_value_2_1346 = outflow_potential_dataset_score_value_1_1345["outflow"]
							outflow_potential_dataset_score_index_3_1347 = outflow_potential_dataset_name_index_3_1335
							outflow_potential_dataset_score_value_3_1348 = outflow_potential_dataset_score_value_2_1346[outflow_potential_dataset_score_index_3_1347]
							if not ("potential_dataset" in outflow_potential_dataset_score_value_3_1348):
								pass
							else:
								outflow_potential_dataset_score_value_4_1349 = outflow_potential_dataset_score_value_3_1348["potential_dataset"]
								outflow_potential_dataset_score_index_5_1350 = outflow_potential_dataset_name_index_5_1340
								outflow_potential_dataset_score_value_5_1351 = outflow_potential_dataset_score_value_4_1349[outflow_potential_dataset_score_index_5_1350]
								outflow_potential_dataset_score_value_6_1352 = outflow_potential_dataset_score_value_5_1351["relevance_score"]
								if True:
									writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", outflow_potential_dataset_score_value_6_1352, None)
						
						writer_2.end_record()
	
	# Transform records of class mndr:Document:6
	outflow_id_document_value_0_1353 = resource_data_1["MineralSystem"]
	start_1354 = 0
	end_1355 = len(outflow_id_document_value_0_1353)
	for outflow_id_document_index_1_1356 in range(start_1354, end_1355):
		outflow_id_document_value_1_1357 = outflow_id_document_value_0_1353[outflow_id_document_index_1_1356]
		if not ("outflow" in outflow_id_document_value_1_1357):
			continue
		else:
			outflow_id_document_value_2_1358 = outflow_id_document_value_1_1357["outflow"]
			start_1359 = 0
			end_1360 = len(outflow_id_document_value_2_1358)
			for outflow_id_document_index_3_1361 in range(start_1359, end_1360):
				outflow_id_document_value_3_1362 = outflow_id_document_value_2_1358[outflow_id_document_index_3_1361]
				if not ("supporting_references" in outflow_id_document_value_3_1362):
					continue
				else:
					outflow_id_document_value_4_1363 = outflow_id_document_value_3_1362["supporting_references"]
					start_1364 = 0
					end_1365 = len(outflow_id_document_value_4_1363)
					for outflow_id_document_index_5_1366 in range(start_1364, end_1365):
						outflow_id_document_value_5_1367 = outflow_id_document_value_4_1363[outflow_id_document_index_5_1366]
						if not ("document" in outflow_id_document_value_5_1367):
							continue
						else:
							outflow_id_document_value_6_1368 = outflow_id_document_value_5_1367["document"]
							outflow_id_document_value_7_1369 = outflow_id_document_value_6_1368["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Document", outflow_id_document_value_7_1369, False, False)
							
							# Retrieve value of data property: outflow_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/id", outflow_id_document_value_7_1369, None)
							
							# Retrieve value of data property: outflow_uri_document
							outflow_uri_document_value_0_1370 = resource_data_1["MineralSystem"]
							outflow_uri_document_index_1_1371 = outflow_id_document_index_1_1356
							outflow_uri_document_value_1_1372 = outflow_uri_document_value_0_1370[outflow_uri_document_index_1_1371]
							if not ("outflow" in outflow_uri_document_value_1_1372):
								pass
							else:
								outflow_uri_document_value_2_1373 = outflow_uri_document_value_1_1372["outflow"]
								outflow_uri_document_index_3_1374 = outflow_id_document_index_3_1361
								outflow_uri_document_value_3_1375 = outflow_uri_document_value_2_1373[outflow_uri_document_index_3_1374]
								if not ("supporting_references" in outflow_uri_document_value_3_1375):
									pass
								else:
									outflow_uri_document_value_4_1376 = outflow_uri_document_value_3_1375["supporting_references"]
									outflow_uri_document_index_5_1377 = outflow_id_document_index_5_1366
									outflow_uri_document_value_5_1378 = outflow_uri_document_value_4_1376[outflow_uri_document_index_5_1377]
									if not ("document" in outflow_uri_document_value_5_1378):
										pass
									else:
										outflow_uri_document_value_6_1379 = outflow_uri_document_value_5_1378["document"]
										if not ("uri" in outflow_uri_document_value_6_1379):
											pass
										else:
											outflow_uri_document_value_7_1380 = outflow_uri_document_value_6_1379["uri"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/uri", outflow_uri_document_value_7_1380, None)
							
							# Retrieve value of data property: outflow_doi
							outflow_doi_value_0_1381 = resource_data_1["MineralSystem"]
							outflow_doi_index_1_1382 = outflow_id_document_index_1_1356
							outflow_doi_value_1_1383 = outflow_doi_value_0_1381[outflow_doi_index_1_1382]
							if not ("outflow" in outflow_doi_value_1_1383):
								pass
							else:
								outflow_doi_value_2_1384 = outflow_doi_value_1_1383["outflow"]
								outflow_doi_index_3_1385 = outflow_id_document_index_3_1361
								outflow_doi_value_3_1386 = outflow_doi_value_2_1384[outflow_doi_index_3_1385]
								if not ("supporting_references" in outflow_doi_value_3_1386):
									pass
								else:
									outflow_doi_value_4_1387 = outflow_doi_value_3_1386["supporting_references"]
									outflow_doi_index_5_1388 = outflow_id_document_index_5_1366
									outflow_doi_value_5_1389 = outflow_doi_value_4_1387[outflow_doi_index_5_1388]
									if not ("document" in outflow_doi_value_5_1389):
										pass
									else:
										outflow_doi_value_6_1390 = outflow_doi_value_5_1389["document"]
										if not ("doi" in outflow_doi_value_6_1390):
											pass
										else:
											outflow_doi_value_7_1391 = outflow_doi_value_6_1390["doi"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/doi", outflow_doi_value_7_1391, None)
							
							# Retrieve value of data property: outflow_journal
							outflow_journal_value_0_1392 = resource_data_1["MineralSystem"]
							outflow_journal_index_1_1393 = outflow_id_document_index_1_1356
							outflow_journal_value_1_1394 = outflow_journal_value_0_1392[outflow_journal_index_1_1393]
							if not ("outflow" in outflow_journal_value_1_1394):
								pass
							else:
								outflow_journal_value_2_1395 = outflow_journal_value_1_1394["outflow"]
								outflow_journal_index_3_1396 = outflow_id_document_index_3_1361
								outflow_journal_value_3_1397 = outflow_journal_value_2_1395[outflow_journal_index_3_1396]
								if not ("supporting_references" in outflow_journal_value_3_1397):
									pass
								else:
									outflow_journal_value_4_1398 = outflow_journal_value_3_1397["supporting_references"]
									outflow_journal_index_5_1399 = outflow_id_document_index_5_1366
									outflow_journal_value_5_1400 = outflow_journal_value_4_1398[outflow_journal_index_5_1399]
									if not ("document" in outflow_journal_value_5_1400):
										pass
									else:
										outflow_journal_value_6_1401 = outflow_journal_value_5_1400["document"]
										if not ("journal" in outflow_journal_value_6_1401):
											pass
										else:
											outflow_journal_value_7_1402 = outflow_journal_value_6_1401["journal"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/journal", outflow_journal_value_7_1402, None)
							
							# Retrieve value of data property: outflow_authors
							outflow_authors_value_0_1403 = resource_data_1["MineralSystem"]
							outflow_authors_index_1_1404 = outflow_id_document_index_1_1356
							outflow_authors_value_1_1405 = outflow_authors_value_0_1403[outflow_authors_index_1_1404]
							if not ("outflow" in outflow_authors_value_1_1405):
								pass
							else:
								outflow_authors_value_2_1406 = outflow_authors_value_1_1405["outflow"]
								outflow_authors_index_3_1407 = outflow_id_document_index_3_1361
								outflow_authors_value_3_1408 = outflow_authors_value_2_1406[outflow_authors_index_3_1407]
								if not ("supporting_references" in outflow_authors_value_3_1408):
									pass
								else:
									outflow_authors_value_4_1409 = outflow_authors_value_3_1408["supporting_references"]
									outflow_authors_index_5_1410 = outflow_id_document_index_5_1366
									outflow_authors_value_5_1411 = outflow_authors_value_4_1409[outflow_authors_index_5_1410]
									if not ("document" in outflow_authors_value_5_1411):
										pass
									else:
										outflow_authors_value_6_1412 = outflow_authors_value_5_1411["document"]
										if not ("authors" in outflow_authors_value_6_1412):
											pass
										else:
											outflow_authors_value_7_1413 = outflow_authors_value_6_1412["authors"]
											start_1414 = 0
											end_1415 = len(outflow_authors_value_7_1413)
											for outflow_authors_index_8_1416 in range(start_1414, end_1415):
												outflow_authors_value_8_1417 = outflow_authors_value_7_1413[outflow_authors_index_8_1416]
												if True:
													writer_2.write_data_property("https://minmod.isi.edu/resource/authors", outflow_authors_value_8_1417, None)
							
							# Retrieve value of data property: outflow_description_document
							outflow_description_document_value_0_1418 = resource_data_1["MineralSystem"]
							outflow_description_document_index_1_1419 = outflow_id_document_index_1_1356
							outflow_description_document_value_1_1420 = outflow_description_document_value_0_1418[outflow_description_document_index_1_1419]
							if not ("outflow" in outflow_description_document_value_1_1420):
								pass
							else:
								outflow_description_document_value_2_1421 = outflow_description_document_value_1_1420["outflow"]
								outflow_description_document_index_3_1422 = outflow_id_document_index_3_1361
								outflow_description_document_value_3_1423 = outflow_description_document_value_2_1421[outflow_description_document_index_3_1422]
								if not ("supporting_references" in outflow_description_document_value_3_1423):
									pass
								else:
									outflow_description_document_value_4_1424 = outflow_description_document_value_3_1423["supporting_references"]
									outflow_description_document_index_5_1425 = outflow_id_document_index_5_1366
									outflow_description_document_value_5_1426 = outflow_description_document_value_4_1424[outflow_description_document_index_5_1425]
									if not ("document" in outflow_description_document_value_5_1426):
										pass
									else:
										outflow_description_document_value_6_1427 = outflow_description_document_value_5_1426["document"]
										if not ("description" in outflow_description_document_value_6_1427):
											pass
										else:
											outflow_description_document_value_7_1428 = outflow_description_document_value_6_1427["description"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/description", outflow_description_document_value_7_1428, None)
							
							# Retrieve value of data property: outflow_title_document
							outflow_title_document_value_0_1429 = resource_data_1["MineralSystem"]
							outflow_title_document_index_1_1430 = outflow_id_document_index_1_1356
							outflow_title_document_value_1_1431 = outflow_title_document_value_0_1429[outflow_title_document_index_1_1430]
							if not ("outflow" in outflow_title_document_value_1_1431):
								pass
							else:
								outflow_title_document_value_2_1432 = outflow_title_document_value_1_1431["outflow"]
								outflow_title_document_index_3_1433 = outflow_id_document_index_3_1361
								outflow_title_document_value_3_1434 = outflow_title_document_value_2_1432[outflow_title_document_index_3_1433]
								if not ("supporting_references" in outflow_title_document_value_3_1434):
									pass
								else:
									outflow_title_document_value_4_1435 = outflow_title_document_value_3_1434["supporting_references"]
									outflow_title_document_index_5_1436 = outflow_id_document_index_5_1366
									outflow_title_document_value_5_1437 = outflow_title_document_value_4_1435[outflow_title_document_index_5_1436]
									if not ("document" in outflow_title_document_value_5_1437):
										pass
									else:
										outflow_title_document_value_6_1438 = outflow_title_document_value_5_1437["document"]
										if not ("title" in outflow_title_document_value_6_1438):
											pass
										else:
											outflow_title_document_value_7_1439 = outflow_title_document_value_6_1438["title"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/title", outflow_title_document_value_7_1439, None)
							
							# Retrieve value of data property: outflow_volume
							outflow_volume_value_0_1440 = resource_data_1["MineralSystem"]
							outflow_volume_index_1_1441 = outflow_id_document_index_1_1356
							outflow_volume_value_1_1442 = outflow_volume_value_0_1440[outflow_volume_index_1_1441]
							if not ("outflow" in outflow_volume_value_1_1442):
								pass
							else:
								outflow_volume_value_2_1443 = outflow_volume_value_1_1442["outflow"]
								outflow_volume_index_3_1444 = outflow_id_document_index_3_1361
								outflow_volume_value_3_1445 = outflow_volume_value_2_1443[outflow_volume_index_3_1444]
								if not ("supporting_references" in outflow_volume_value_3_1445):
									pass
								else:
									outflow_volume_value_4_1446 = outflow_volume_value_3_1445["supporting_references"]
									outflow_volume_index_5_1447 = outflow_id_document_index_5_1366
									outflow_volume_value_5_1448 = outflow_volume_value_4_1446[outflow_volume_index_5_1447]
									if not ("document" in outflow_volume_value_5_1448):
										pass
									else:
										outflow_volume_value_6_1449 = outflow_volume_value_5_1448["document"]
										if not ("volume" in outflow_volume_value_6_1449):
											pass
										else:
											outflow_volume_value_7_1450 = outflow_volume_value_6_1449["volume"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/volume", outflow_volume_value_7_1450, None)
							
							# Retrieve value of data property: outflow_issue_document
							outflow_issue_document_value_0_1451 = resource_data_1["MineralSystem"]
							outflow_issue_document_index_1_1452 = outflow_id_document_index_1_1356
							outflow_issue_document_value_1_1453 = outflow_issue_document_value_0_1451[outflow_issue_document_index_1_1452]
							if not ("outflow" in outflow_issue_document_value_1_1453):
								pass
							else:
								outflow_issue_document_value_2_1454 = outflow_issue_document_value_1_1453["outflow"]
								outflow_issue_document_index_3_1455 = outflow_id_document_index_3_1361
								outflow_issue_document_value_3_1456 = outflow_issue_document_value_2_1454[outflow_issue_document_index_3_1455]
								if not ("supporting_references" in outflow_issue_document_value_3_1456):
									pass
								else:
									outflow_issue_document_value_4_1457 = outflow_issue_document_value_3_1456["supporting_references"]
									outflow_issue_document_index_5_1458 = outflow_id_document_index_5_1366
									outflow_issue_document_value_5_1459 = outflow_issue_document_value_4_1457[outflow_issue_document_index_5_1458]
									if not ("document" in outflow_issue_document_value_5_1459):
										pass
									else:
										outflow_issue_document_value_6_1460 = outflow_issue_document_value_5_1459["document"]
										if not ("issue" in outflow_issue_document_value_6_1460):
											pass
										else:
											outflow_issue_document_value_7_1461 = outflow_issue_document_value_6_1460["issue"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/issue", outflow_issue_document_value_7_1461, None)
							
							# Retrieve value of data property: outflow_month_document
							outflow_month_document_value_0_1462 = resource_data_1["MineralSystem"]
							outflow_month_document_index_1_1463 = outflow_id_document_index_1_1356
							outflow_month_document_value_1_1464 = outflow_month_document_value_0_1462[outflow_month_document_index_1_1463]
							if not ("outflow" in outflow_month_document_value_1_1464):
								pass
							else:
								outflow_month_document_value_2_1465 = outflow_month_document_value_1_1464["outflow"]
								outflow_month_document_index_3_1466 = outflow_id_document_index_3_1361
								outflow_month_document_value_3_1467 = outflow_month_document_value_2_1465[outflow_month_document_index_3_1466]
								if not ("supporting_references" in outflow_month_document_value_3_1467):
									pass
								else:
									outflow_month_document_value_4_1468 = outflow_month_document_value_3_1467["supporting_references"]
									outflow_month_document_index_5_1469 = outflow_id_document_index_5_1366
									outflow_month_document_value_5_1470 = outflow_month_document_value_4_1468[outflow_month_document_index_5_1469]
									if not ("document" in outflow_month_document_value_5_1470):
										pass
									else:
										outflow_month_document_value_6_1471 = outflow_month_document_value_5_1470["document"]
										if not ("month" in outflow_month_document_value_6_1471):
											pass
										else:
											outflow_month_document_value_7_1472 = outflow_month_document_value_6_1471["month"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/month", outflow_month_document_value_7_1472, None)
							
							# Retrieve value of data property: outflow_year_document
							outflow_year_document_value_0_1473 = resource_data_1["MineralSystem"]
							outflow_year_document_index_1_1474 = outflow_id_document_index_1_1356
							outflow_year_document_value_1_1475 = outflow_year_document_value_0_1473[outflow_year_document_index_1_1474]
							if not ("outflow" in outflow_year_document_value_1_1475):
								pass
							else:
								outflow_year_document_value_2_1476 = outflow_year_document_value_1_1475["outflow"]
								outflow_year_document_index_3_1477 = outflow_id_document_index_3_1361
								outflow_year_document_value_3_1478 = outflow_year_document_value_2_1476[outflow_year_document_index_3_1477]
								if not ("supporting_references" in outflow_year_document_value_3_1478):
									pass
								else:
									outflow_year_document_value_4_1479 = outflow_year_document_value_3_1478["supporting_references"]
									outflow_year_document_index_5_1480 = outflow_id_document_index_5_1366
									outflow_year_document_value_5_1481 = outflow_year_document_value_4_1479[outflow_year_document_index_5_1480]
									if not ("document" in outflow_year_document_value_5_1481):
										pass
									else:
										outflow_year_document_value_6_1482 = outflow_year_document_value_5_1481["document"]
										if not ("year" in outflow_year_document_value_6_1482):
											pass
										else:
											outflow_year_document_value_7_1483 = outflow_year_document_value_6_1482["year"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/year", outflow_year_document_value_7_1483, None)
							
							writer_2.end_record()
	
	# Transform records of class mndr:BoundingBox:6
	outflow_x_min_value_0_1484 = resource_data_1["MineralSystem"]
	start_1485 = 0
	end_1486 = len(outflow_x_min_value_0_1484)
	for outflow_x_min_index_1_1487 in range(start_1485, end_1486):
		outflow_x_min_value_1_1488 = outflow_x_min_value_0_1484[outflow_x_min_index_1_1487]
		if not ("outflow" in outflow_x_min_value_1_1488):
			continue
		else:
			outflow_x_min_value_2_1489 = outflow_x_min_value_1_1488["outflow"]
			start_1490 = 0
			end_1491 = len(outflow_x_min_value_2_1489)
			for outflow_x_min_index_3_1492 in range(start_1490, end_1491):
				outflow_x_min_value_3_1493 = outflow_x_min_value_2_1489[outflow_x_min_index_3_1492]
				if not ("supporting_references" in outflow_x_min_value_3_1493):
					continue
				else:
					outflow_x_min_value_4_1494 = outflow_x_min_value_3_1493["supporting_references"]
					start_1495 = 0
					end_1496 = len(outflow_x_min_value_4_1494)
					for outflow_x_min_index_5_1497 in range(start_1495, end_1496):
						outflow_x_min_value_5_1498 = outflow_x_min_value_4_1494[outflow_x_min_index_5_1497]
						if not ("page_info" in outflow_x_min_value_5_1498):
							continue
						else:
							outflow_x_min_value_6_1499 = outflow_x_min_value_5_1498["page_info"]
							start_1500 = 0
							end_1501 = len(outflow_x_min_value_6_1499)
							for outflow_x_min_index_7_1502 in range(start_1500, end_1501):
								outflow_x_min_value_7_1503 = outflow_x_min_value_6_1499[outflow_x_min_index_7_1502]
								if not ("bounding_box" in outflow_x_min_value_7_1503):
									continue
								else:
									outflow_x_min_value_8_1504 = outflow_x_min_value_7_1503["bounding_box"]
									if not ("x_min" in outflow_x_min_value_8_1504):
										continue
									else:
										outflow_x_min_value_9_1505 = outflow_x_min_value_8_1504["x_min"]
										writer_2.begin_record("https://minmod.isi.edu/resource/BoundingBox", (130, outflow_x_min_index_1_1487, outflow_x_min_index_3_1492, outflow_x_min_index_5_1497, outflow_x_min_index_7_1502), True, False)
										
										# Retrieve value of data property: outflow_x_min
										if True:
											writer_2.write_data_property("https://minmod.isi.edu/resource/x_min", outflow_x_min_value_9_1505, None)
										
										# Retrieve value of data property: outflow_x_max
										outflow_x_max_value_0_1506 = resource_data_1["MineralSystem"]
										outflow_x_max_index_1_1507 = outflow_x_min_index_1_1487
										outflow_x_max_value_1_1508 = outflow_x_max_value_0_1506[outflow_x_max_index_1_1507]
										if not ("outflow" in outflow_x_max_value_1_1508):
											pass
										else:
											outflow_x_max_value_2_1509 = outflow_x_max_value_1_1508["outflow"]
											outflow_x_max_index_3_1510 = outflow_x_min_index_3_1492
											outflow_x_max_value_3_1511 = outflow_x_max_value_2_1509[outflow_x_max_index_3_1510]
											if not ("supporting_references" in outflow_x_max_value_3_1511):
												pass
											else:
												outflow_x_max_value_4_1512 = outflow_x_max_value_3_1511["supporting_references"]
												outflow_x_max_index_5_1513 = outflow_x_min_index_5_1497
												outflow_x_max_value_5_1514 = outflow_x_max_value_4_1512[outflow_x_max_index_5_1513]
												if not ("page_info" in outflow_x_max_value_5_1514):
													pass
												else:
													outflow_x_max_value_6_1515 = outflow_x_max_value_5_1514["page_info"]
													outflow_x_max_index_7_1516 = outflow_x_min_index_7_1502
													outflow_x_max_value_7_1517 = outflow_x_max_value_6_1515[outflow_x_max_index_7_1516]
													if not ("bounding_box" in outflow_x_max_value_7_1517):
														pass
													else:
														outflow_x_max_value_8_1518 = outflow_x_max_value_7_1517["bounding_box"]
														if not ("x_max" in outflow_x_max_value_8_1518):
															pass
														else:
															outflow_x_max_value_9_1519 = outflow_x_max_value_8_1518["x_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/x_max", outflow_x_max_value_9_1519, None)
										
										# Retrieve value of data property: outflow_y_min
										outflow_y_min_value_0_1520 = resource_data_1["MineralSystem"]
										outflow_y_min_index_1_1521 = outflow_x_min_index_1_1487
										outflow_y_min_value_1_1522 = outflow_y_min_value_0_1520[outflow_y_min_index_1_1521]
										if not ("outflow" in outflow_y_min_value_1_1522):
											pass
										else:
											outflow_y_min_value_2_1523 = outflow_y_min_value_1_1522["outflow"]
											outflow_y_min_index_3_1524 = outflow_x_min_index_3_1492
											outflow_y_min_value_3_1525 = outflow_y_min_value_2_1523[outflow_y_min_index_3_1524]
											if not ("supporting_references" in outflow_y_min_value_3_1525):
												pass
											else:
												outflow_y_min_value_4_1526 = outflow_y_min_value_3_1525["supporting_references"]
												outflow_y_min_index_5_1527 = outflow_x_min_index_5_1497
												outflow_y_min_value_5_1528 = outflow_y_min_value_4_1526[outflow_y_min_index_5_1527]
												if not ("page_info" in outflow_y_min_value_5_1528):
													pass
												else:
													outflow_y_min_value_6_1529 = outflow_y_min_value_5_1528["page_info"]
													outflow_y_min_index_7_1530 = outflow_x_min_index_7_1502
													outflow_y_min_value_7_1531 = outflow_y_min_value_6_1529[outflow_y_min_index_7_1530]
													if not ("bounding_box" in outflow_y_min_value_7_1531):
														pass
													else:
														outflow_y_min_value_8_1532 = outflow_y_min_value_7_1531["bounding_box"]
														if not ("y_min" in outflow_y_min_value_8_1532):
															pass
														else:
															outflow_y_min_value_9_1533 = outflow_y_min_value_8_1532["y_min"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_min", outflow_y_min_value_9_1533, None)
										
										# Retrieve value of data property: outflow_y_max
										outflow_y_max_value_0_1534 = resource_data_1["MineralSystem"]
										outflow_y_max_index_1_1535 = outflow_x_min_index_1_1487
										outflow_y_max_value_1_1536 = outflow_y_max_value_0_1534[outflow_y_max_index_1_1535]
										if not ("outflow" in outflow_y_max_value_1_1536):
											pass
										else:
											outflow_y_max_value_2_1537 = outflow_y_max_value_1_1536["outflow"]
											outflow_y_max_index_3_1538 = outflow_x_min_index_3_1492
											outflow_y_max_value_3_1539 = outflow_y_max_value_2_1537[outflow_y_max_index_3_1538]
											if not ("supporting_references" in outflow_y_max_value_3_1539):
												pass
											else:
												outflow_y_max_value_4_1540 = outflow_y_max_value_3_1539["supporting_references"]
												outflow_y_max_index_5_1541 = outflow_x_min_index_5_1497
												outflow_y_max_value_5_1542 = outflow_y_max_value_4_1540[outflow_y_max_index_5_1541]
												if not ("page_info" in outflow_y_max_value_5_1542):
													pass
												else:
													outflow_y_max_value_6_1543 = outflow_y_max_value_5_1542["page_info"]
													outflow_y_max_index_7_1544 = outflow_x_min_index_7_1502
													outflow_y_max_value_7_1545 = outflow_y_max_value_6_1543[outflow_y_max_index_7_1544]
													if not ("bounding_box" in outflow_y_max_value_7_1545):
														pass
													else:
														outflow_y_max_value_8_1546 = outflow_y_max_value_7_1545["bounding_box"]
														if not ("y_max" in outflow_y_max_value_8_1546):
															pass
														else:
															outflow_y_max_value_9_1547 = outflow_y_max_value_8_1546["y_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_max", outflow_y_max_value_9_1547, None)
										
										writer_2.end_record()
	
	# Transform records of class mndr:PageInfo:6
	outflow_page_value_0_1548 = resource_data_1["MineralSystem"]
	start_1549 = 0
	end_1550 = len(outflow_page_value_0_1548)
	for outflow_page_index_1_1551 in range(start_1549, end_1550):
		outflow_page_value_1_1552 = outflow_page_value_0_1548[outflow_page_index_1_1551]
		if not ("outflow" in outflow_page_value_1_1552):
			continue
		else:
			outflow_page_value_2_1553 = outflow_page_value_1_1552["outflow"]
			start_1554 = 0
			end_1555 = len(outflow_page_value_2_1553)
			for outflow_page_index_3_1556 in range(start_1554, end_1555):
				outflow_page_value_3_1557 = outflow_page_value_2_1553[outflow_page_index_3_1556]
				if not ("supporting_references" in outflow_page_value_3_1557):
					continue
				else:
					outflow_page_value_4_1558 = outflow_page_value_3_1557["supporting_references"]
					start_1559 = 0
					end_1560 = len(outflow_page_value_4_1558)
					for outflow_page_index_5_1561 in range(start_1559, end_1560):
						outflow_page_value_5_1562 = outflow_page_value_4_1558[outflow_page_index_5_1561]
						if not ("page_info" in outflow_page_value_5_1562):
							continue
						else:
							outflow_page_value_6_1563 = outflow_page_value_5_1562["page_info"]
							start_1564 = 0
							end_1565 = len(outflow_page_value_6_1563)
							for outflow_page_index_7_1566 in range(start_1564, end_1565):
								outflow_page_value_7_1567 = outflow_page_value_6_1563[outflow_page_index_7_1566]
								if not ("page" in outflow_page_value_7_1567):
									continue
								else:
									outflow_page_value_8_1568 = outflow_page_value_7_1567["page"]
									writer_2.begin_record("https://minmod.isi.edu/resource/PageInfo", (128, outflow_page_index_1_1551, outflow_page_index_3_1556, outflow_page_index_5_1561, outflow_page_index_7_1566), True, False)
									
									# Retrieve value of data property: outflow_page
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/page", outflow_page_value_8_1568, None)
									
									# Retrieve value of object property: outflow_x_min
									outflow_x_min_value_0_1569 = resource_data_1["MineralSystem"]
									outflow_x_min_index_1_1570 = outflow_page_index_1_1551
									outflow_x_min_value_1_1571 = outflow_x_min_value_0_1569[outflow_x_min_index_1_1570]
									if not ("outflow" in outflow_x_min_value_1_1571):
										pass
									else:
										outflow_x_min_value_2_1572 = outflow_x_min_value_1_1571["outflow"]
										outflow_x_min_index_3_1573 = outflow_page_index_3_1556
										outflow_x_min_value_3_1574 = outflow_x_min_value_2_1572[outflow_x_min_index_3_1573]
										if not ("supporting_references" in outflow_x_min_value_3_1574):
											pass
										else:
											outflow_x_min_value_4_1575 = outflow_x_min_value_3_1574["supporting_references"]
											outflow_x_min_index_5_1576 = outflow_page_index_5_1561
											outflow_x_min_value_5_1577 = outflow_x_min_value_4_1575[outflow_x_min_index_5_1576]
											if not ("page_info" in outflow_x_min_value_5_1577):
												pass
											else:
												outflow_x_min_value_6_1578 = outflow_x_min_value_5_1577["page_info"]
												outflow_x_min_index_7_1579 = outflow_page_index_7_1566
												outflow_x_min_value_7_1580 = outflow_x_min_value_6_1578[outflow_x_min_index_7_1579]
												if not ("bounding_box" in outflow_x_min_value_7_1580):
													pass
												else:
													outflow_x_min_value_8_1581 = outflow_x_min_value_7_1580["bounding_box"]
													if not ("x_min" in outflow_x_min_value_8_1581):
														pass
													else:
														outflow_x_min_value_9_1582 = outflow_x_min_value_8_1581["x_min"]
														if writer_2.has_written_record((130, outflow_x_min_index_1_1570, outflow_x_min_index_3_1573, outflow_x_min_index_5_1576, outflow_x_min_index_7_1579)):
															writer_2.write_object_property("https://minmod.isi.edu/resource/bounding_box", (130, outflow_x_min_index_1_1570, outflow_x_min_index_3_1573, outflow_x_min_index_5_1576, outflow_x_min_index_7_1579), True, True, False)
									
									writer_2.end_record()
	
	# Transform records of class mndr:Reference:6
	outflow_id_document_value_0_1583 = resource_data_1["MineralSystem"]
	start_1584 = 0
	end_1585 = len(outflow_id_document_value_0_1583)
	for outflow_id_document_index_1_1586 in range(start_1584, end_1585):
		outflow_id_document_value_1_1587 = outflow_id_document_value_0_1583[outflow_id_document_index_1_1586]
		if not ("outflow" in outflow_id_document_value_1_1587):
			continue
		else:
			outflow_id_document_value_2_1588 = outflow_id_document_value_1_1587["outflow"]
			start_1589 = 0
			end_1590 = len(outflow_id_document_value_2_1588)
			for outflow_id_document_index_3_1591 in range(start_1589, end_1590):
				outflow_id_document_value_3_1592 = outflow_id_document_value_2_1588[outflow_id_document_index_3_1591]
				if not ("supporting_references" in outflow_id_document_value_3_1592):
					continue
				else:
					outflow_id_document_value_4_1593 = outflow_id_document_value_3_1592["supporting_references"]
					start_1594 = 0
					end_1595 = len(outflow_id_document_value_4_1593)
					for outflow_id_document_index_5_1596 in range(start_1594, end_1595):
						outflow_id_document_value_5_1597 = outflow_id_document_value_4_1593[outflow_id_document_index_5_1596]
						if not ("document" in outflow_id_document_value_5_1597):
							continue
						else:
							outflow_id_document_value_6_1598 = outflow_id_document_value_5_1597["document"]
							outflow_id_document_value_7_1599 = outflow_id_document_value_6_1598["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (118, outflow_id_document_index_1_1586, outflow_id_document_index_3_1591, outflow_id_document_index_5_1596), True, False)
							
							# Retrieve value of data property: outflow_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/document_id", outflow_id_document_value_7_1599, None)
							
							# Retrieve value of object property: outflow_id_document
							if writer_2.has_written_record(outflow_id_document_value_7_1599):
								writer_2.write_object_property("https://minmod.isi.edu/resource/document", outflow_id_document_value_7_1599, True, False, False)
							
							# Retrieve value of object property: outflow_page
							outflow_page_value_0_1600 = resource_data_1["MineralSystem"]
							outflow_page_index_1_1601 = outflow_id_document_index_1_1586
							outflow_page_value_1_1602 = outflow_page_value_0_1600[outflow_page_index_1_1601]
							if not ("outflow" in outflow_page_value_1_1602):
								pass
							else:
								outflow_page_value_2_1603 = outflow_page_value_1_1602["outflow"]
								outflow_page_index_3_1604 = outflow_id_document_index_3_1591
								outflow_page_value_3_1605 = outflow_page_value_2_1603[outflow_page_index_3_1604]
								if not ("supporting_references" in outflow_page_value_3_1605):
									pass
								else:
									outflow_page_value_4_1606 = outflow_page_value_3_1605["supporting_references"]
									outflow_page_index_5_1607 = outflow_id_document_index_5_1596
									outflow_page_value_5_1608 = outflow_page_value_4_1606[outflow_page_index_5_1607]
									if not ("page_info" in outflow_page_value_5_1608):
										pass
									else:
										outflow_page_value_6_1609 = outflow_page_value_5_1608["page_info"]
										start_1610 = 0
										end_1611 = len(outflow_page_value_6_1609)
										for outflow_page_index_7_1612 in range(start_1610, end_1611):
											outflow_page_value_7_1613 = outflow_page_value_6_1609[outflow_page_index_7_1612]
											if not ("page" in outflow_page_value_7_1613):
												pass
											else:
												outflow_page_value_8_1614 = outflow_page_value_7_1613["page"]
												if writer_2.has_written_record((128, outflow_page_index_1_1601, outflow_page_index_3_1604, outflow_page_index_5_1607, outflow_page_index_7_1612)):
													writer_2.write_object_property("https://minmod.isi.edu/resource/page_info", (128, outflow_page_index_1_1601, outflow_page_index_3_1604, outflow_page_index_5_1607, outflow_page_index_7_1612), True, True, False)
							
							writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:6
	outflow_criteria_value_0_1615 = resource_data_1["MineralSystem"]
	start_1616 = 0
	end_1617 = len(outflow_criteria_value_0_1615)
	for outflow_criteria_index_1_1618 in range(start_1616, end_1617):
		outflow_criteria_value_1_1619 = outflow_criteria_value_0_1615[outflow_criteria_index_1_1618]
		if not ("outflow" in outflow_criteria_value_1_1619):
			continue
		else:
			outflow_criteria_value_2_1620 = outflow_criteria_value_1_1619["outflow"]
			start_1621 = 0
			end_1622 = len(outflow_criteria_value_2_1620)
			for outflow_criteria_index_3_1623 in range(start_1621, end_1622):
				outflow_criteria_value_3_1624 = outflow_criteria_value_2_1620[outflow_criteria_index_3_1623]
				outflow_criteria_value_4_1625 = outflow_criteria_value_3_1624["criteria"]
				writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (112, outflow_criteria_index_1_1618, outflow_criteria_index_3_1623), True, False)
				
				# Retrieve value of data property: outflow_criteria
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", outflow_criteria_value_4_1625, None)
				
				# Retrieve value of data property: outflow_theoretical
				outflow_theoretical_value_0_1626 = resource_data_1["MineralSystem"]
				outflow_theoretical_index_1_1627 = outflow_criteria_index_1_1618
				outflow_theoretical_value_1_1628 = outflow_theoretical_value_0_1626[outflow_theoretical_index_1_1627]
				if not ("outflow" in outflow_theoretical_value_1_1628):
					pass
				else:
					outflow_theoretical_value_2_1629 = outflow_theoretical_value_1_1628["outflow"]
					outflow_theoretical_index_3_1630 = outflow_criteria_index_3_1623
					outflow_theoretical_value_3_1631 = outflow_theoretical_value_2_1629[outflow_theoretical_index_3_1630]
					if not ("theoretical" in outflow_theoretical_value_3_1631):
						pass
					else:
						outflow_theoretical_value_4_1632 = outflow_theoretical_value_3_1631["theoretical"]
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/theoretical", outflow_theoretical_value_4_1632, None)
				
				# Retrieve value of object property: outflow_potential_dataset_name
				outflow_potential_dataset_name_value_0_1633 = resource_data_1["MineralSystem"]
				outflow_potential_dataset_name_index_1_1634 = outflow_criteria_index_1_1618
				outflow_potential_dataset_name_value_1_1635 = outflow_potential_dataset_name_value_0_1633[outflow_potential_dataset_name_index_1_1634]
				if not ("outflow" in outflow_potential_dataset_name_value_1_1635):
					pass
				else:
					outflow_potential_dataset_name_value_2_1636 = outflow_potential_dataset_name_value_1_1635["outflow"]
					outflow_potential_dataset_name_index_3_1637 = outflow_criteria_index_3_1623
					outflow_potential_dataset_name_value_3_1638 = outflow_potential_dataset_name_value_2_1636[outflow_potential_dataset_name_index_3_1637]
					if not ("potential_dataset" in outflow_potential_dataset_name_value_3_1638):
						pass
					else:
						outflow_potential_dataset_name_value_4_1639 = outflow_potential_dataset_name_value_3_1638["potential_dataset"]
						start_1640 = 0
						end_1641 = len(outflow_potential_dataset_name_value_4_1639)
						for outflow_potential_dataset_name_index_5_1642 in range(start_1640, end_1641):
							outflow_potential_dataset_name_value_5_1643 = outflow_potential_dataset_name_value_4_1639[outflow_potential_dataset_name_index_5_1642]
							outflow_potential_dataset_name_value_6_1644 = outflow_potential_dataset_name_value_5_1643["name"]
							if writer_2.has_written_record((114, outflow_potential_dataset_name_index_1_1634, outflow_potential_dataset_name_index_3_1637, outflow_potential_dataset_name_index_5_1642)):
								writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (114, outflow_potential_dataset_name_index_1_1634, outflow_potential_dataset_name_index_3_1637, outflow_potential_dataset_name_index_5_1642), True, True, False)
				
				# Retrieve value of object property: outflow_id_document
				outflow_id_document_value_0_1645 = resource_data_1["MineralSystem"]
				outflow_id_document_index_1_1646 = outflow_criteria_index_1_1618
				outflow_id_document_value_1_1647 = outflow_id_document_value_0_1645[outflow_id_document_index_1_1646]
				if not ("outflow" in outflow_id_document_value_1_1647):
					pass
				else:
					outflow_id_document_value_2_1648 = outflow_id_document_value_1_1647["outflow"]
					outflow_id_document_index_3_1649 = outflow_criteria_index_3_1623
					outflow_id_document_value_3_1650 = outflow_id_document_value_2_1648[outflow_id_document_index_3_1649]
					if not ("supporting_references" in outflow_id_document_value_3_1650):
						pass
					else:
						outflow_id_document_value_4_1651 = outflow_id_document_value_3_1650["supporting_references"]
						start_1652 = 0
						end_1653 = len(outflow_id_document_value_4_1651)
						for outflow_id_document_index_5_1654 in range(start_1652, end_1653):
							outflow_id_document_value_5_1655 = outflow_id_document_value_4_1651[outflow_id_document_index_5_1654]
							if not ("document" in outflow_id_document_value_5_1655):
								pass
							else:
								outflow_id_document_value_6_1656 = outflow_id_document_value_5_1655["document"]
								outflow_id_document_value_7_1657 = outflow_id_document_value_6_1656["id"]
								if writer_2.has_written_record((118, outflow_id_document_index_1_1646, outflow_id_document_index_3_1649, outflow_id_document_index_5_1654)):
									writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (118, outflow_id_document_index_1_1646, outflow_id_document_index_3_1649, outflow_id_document_index_5_1654), True, True, False)
				
				writer_2.end_record()
	
	# Transform records of class mndr:EvidenceLayer:5
	energy_potential_dataset_name_value_0_1658 = resource_data_1["MineralSystem"]
	start_1659 = 0
	end_1660 = len(energy_potential_dataset_name_value_0_1658)
	for energy_potential_dataset_name_index_1_1661 in range(start_1659, end_1660):
		energy_potential_dataset_name_value_1_1662 = energy_potential_dataset_name_value_0_1658[energy_potential_dataset_name_index_1_1661]
		if not ("energy" in energy_potential_dataset_name_value_1_1662):
			continue
		else:
			energy_potential_dataset_name_value_2_1663 = energy_potential_dataset_name_value_1_1662["energy"]
			start_1664 = 0
			end_1665 = len(energy_potential_dataset_name_value_2_1663)
			for energy_potential_dataset_name_index_3_1666 in range(start_1664, end_1665):
				energy_potential_dataset_name_value_3_1667 = energy_potential_dataset_name_value_2_1663[energy_potential_dataset_name_index_3_1666]
				if not ("potential_dataset" in energy_potential_dataset_name_value_3_1667):
					continue
				else:
					energy_potential_dataset_name_value_4_1668 = energy_potential_dataset_name_value_3_1667["potential_dataset"]
					start_1669 = 0
					end_1670 = len(energy_potential_dataset_name_value_4_1668)
					for energy_potential_dataset_name_index_5_1671 in range(start_1669, end_1670):
						energy_potential_dataset_name_value_5_1672 = energy_potential_dataset_name_value_4_1668[energy_potential_dataset_name_index_5_1671]
						energy_potential_dataset_name_value_6_1673 = energy_potential_dataset_name_value_5_1672["name"]
						writer_2.begin_record("https://minmod.isi.edu/resource/EvidenceLayer", (92, energy_potential_dataset_name_index_1_1661, energy_potential_dataset_name_index_3_1666, energy_potential_dataset_name_index_5_1671), True, False)
						
						# Retrieve value of data property: energy_potential_dataset_name
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/name", energy_potential_dataset_name_value_6_1673, None)
						
						# Retrieve value of data property: energy_potential_dataset_score
						energy_potential_dataset_score_value_0_1674 = resource_data_1["MineralSystem"]
						energy_potential_dataset_score_index_1_1675 = energy_potential_dataset_name_index_1_1661
						energy_potential_dataset_score_value_1_1676 = energy_potential_dataset_score_value_0_1674[energy_potential_dataset_score_index_1_1675]
						if not ("energy" in energy_potential_dataset_score_value_1_1676):
							pass
						else:
							energy_potential_dataset_score_value_2_1677 = energy_potential_dataset_score_value_1_1676["energy"]
							energy_potential_dataset_score_index_3_1678 = energy_potential_dataset_name_index_3_1666
							energy_potential_dataset_score_value_3_1679 = energy_potential_dataset_score_value_2_1677[energy_potential_dataset_score_index_3_1678]
							if not ("potential_dataset" in energy_potential_dataset_score_value_3_1679):
								pass
							else:
								energy_potential_dataset_score_value_4_1680 = energy_potential_dataset_score_value_3_1679["potential_dataset"]
								energy_potential_dataset_score_index_5_1681 = energy_potential_dataset_name_index_5_1671
								energy_potential_dataset_score_value_5_1682 = energy_potential_dataset_score_value_4_1680[energy_potential_dataset_score_index_5_1681]
								energy_potential_dataset_score_value_6_1683 = energy_potential_dataset_score_value_5_1682["relevance_score"]
								if True:
									writer_2.write_data_property("https://minmod.isi.edu/resource/evidence_score", energy_potential_dataset_score_value_6_1683, None)
						
						writer_2.end_record()
	
	# Transform records of class mndr:Document:5
	energy_id_document_value_0_1684 = resource_data_1["MineralSystem"]
	start_1685 = 0
	end_1686 = len(energy_id_document_value_0_1684)
	for energy_id_document_index_1_1687 in range(start_1685, end_1686):
		energy_id_document_value_1_1688 = energy_id_document_value_0_1684[energy_id_document_index_1_1687]
		if not ("energy" in energy_id_document_value_1_1688):
			continue
		else:
			energy_id_document_value_2_1689 = energy_id_document_value_1_1688["energy"]
			start_1690 = 0
			end_1691 = len(energy_id_document_value_2_1689)
			for energy_id_document_index_3_1692 in range(start_1690, end_1691):
				energy_id_document_value_3_1693 = energy_id_document_value_2_1689[energy_id_document_index_3_1692]
				if not ("supporting_references" in energy_id_document_value_3_1693):
					continue
				else:
					energy_id_document_value_4_1694 = energy_id_document_value_3_1693["supporting_references"]
					start_1695 = 0
					end_1696 = len(energy_id_document_value_4_1694)
					for energy_id_document_index_5_1697 in range(start_1695, end_1696):
						energy_id_document_value_5_1698 = energy_id_document_value_4_1694[energy_id_document_index_5_1697]
						if not ("document" in energy_id_document_value_5_1698):
							continue
						else:
							energy_id_document_value_6_1699 = energy_id_document_value_5_1698["document"]
							energy_id_document_value_7_1700 = energy_id_document_value_6_1699["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Document", energy_id_document_value_7_1700, False, False)
							
							# Retrieve value of data property: energy_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/id", energy_id_document_value_7_1700, None)
							
							# Retrieve value of data property: energy_uri_document
							energy_uri_document_value_0_1701 = resource_data_1["MineralSystem"]
							energy_uri_document_index_1_1702 = energy_id_document_index_1_1687
							energy_uri_document_value_1_1703 = energy_uri_document_value_0_1701[energy_uri_document_index_1_1702]
							if not ("energy" in energy_uri_document_value_1_1703):
								pass
							else:
								energy_uri_document_value_2_1704 = energy_uri_document_value_1_1703["energy"]
								energy_uri_document_index_3_1705 = energy_id_document_index_3_1692
								energy_uri_document_value_3_1706 = energy_uri_document_value_2_1704[energy_uri_document_index_3_1705]
								if not ("supporting_references" in energy_uri_document_value_3_1706):
									pass
								else:
									energy_uri_document_value_4_1707 = energy_uri_document_value_3_1706["supporting_references"]
									energy_uri_document_index_5_1708 = energy_id_document_index_5_1697
									energy_uri_document_value_5_1709 = energy_uri_document_value_4_1707[energy_uri_document_index_5_1708]
									if not ("document" in energy_uri_document_value_5_1709):
										pass
									else:
										energy_uri_document_value_6_1710 = energy_uri_document_value_5_1709["document"]
										if not ("uri" in energy_uri_document_value_6_1710):
											pass
										else:
											energy_uri_document_value_7_1711 = energy_uri_document_value_6_1710["uri"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/uri", energy_uri_document_value_7_1711, None)
							
							# Retrieve value of data property: energy_doi
							energy_doi_value_0_1712 = resource_data_1["MineralSystem"]
							energy_doi_index_1_1713 = energy_id_document_index_1_1687
							energy_doi_value_1_1714 = energy_doi_value_0_1712[energy_doi_index_1_1713]
							if not ("energy" in energy_doi_value_1_1714):
								pass
							else:
								energy_doi_value_2_1715 = energy_doi_value_1_1714["energy"]
								energy_doi_index_3_1716 = energy_id_document_index_3_1692
								energy_doi_value_3_1717 = energy_doi_value_2_1715[energy_doi_index_3_1716]
								if not ("supporting_references" in energy_doi_value_3_1717):
									pass
								else:
									energy_doi_value_4_1718 = energy_doi_value_3_1717["supporting_references"]
									energy_doi_index_5_1719 = energy_id_document_index_5_1697
									energy_doi_value_5_1720 = energy_doi_value_4_1718[energy_doi_index_5_1719]
									if not ("document" in energy_doi_value_5_1720):
										pass
									else:
										energy_doi_value_6_1721 = energy_doi_value_5_1720["document"]
										if not ("doi" in energy_doi_value_6_1721):
											pass
										else:
											energy_doi_value_7_1722 = energy_doi_value_6_1721["doi"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/doi", energy_doi_value_7_1722, None)
							
							# Retrieve value of data property: energy_journal
							energy_journal_value_0_1723 = resource_data_1["MineralSystem"]
							energy_journal_index_1_1724 = energy_id_document_index_1_1687
							energy_journal_value_1_1725 = energy_journal_value_0_1723[energy_journal_index_1_1724]
							if not ("energy" in energy_journal_value_1_1725):
								pass
							else:
								energy_journal_value_2_1726 = energy_journal_value_1_1725["energy"]
								energy_journal_index_3_1727 = energy_id_document_index_3_1692
								energy_journal_value_3_1728 = energy_journal_value_2_1726[energy_journal_index_3_1727]
								if not ("supporting_references" in energy_journal_value_3_1728):
									pass
								else:
									energy_journal_value_4_1729 = energy_journal_value_3_1728["supporting_references"]
									energy_journal_index_5_1730 = energy_id_document_index_5_1697
									energy_journal_value_5_1731 = energy_journal_value_4_1729[energy_journal_index_5_1730]
									if not ("document" in energy_journal_value_5_1731):
										pass
									else:
										energy_journal_value_6_1732 = energy_journal_value_5_1731["document"]
										if not ("journal" in energy_journal_value_6_1732):
											pass
										else:
											energy_journal_value_7_1733 = energy_journal_value_6_1732["journal"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/journal", energy_journal_value_7_1733, None)
							
							# Retrieve value of data property: energy_authors
							energy_authors_value_0_1734 = resource_data_1["MineralSystem"]
							energy_authors_index_1_1735 = energy_id_document_index_1_1687
							energy_authors_value_1_1736 = energy_authors_value_0_1734[energy_authors_index_1_1735]
							if not ("energy" in energy_authors_value_1_1736):
								pass
							else:
								energy_authors_value_2_1737 = energy_authors_value_1_1736["energy"]
								energy_authors_index_3_1738 = energy_id_document_index_3_1692
								energy_authors_value_3_1739 = energy_authors_value_2_1737[energy_authors_index_3_1738]
								if not ("supporting_references" in energy_authors_value_3_1739):
									pass
								else:
									energy_authors_value_4_1740 = energy_authors_value_3_1739["supporting_references"]
									energy_authors_index_5_1741 = energy_id_document_index_5_1697
									energy_authors_value_5_1742 = energy_authors_value_4_1740[energy_authors_index_5_1741]
									if not ("document" in energy_authors_value_5_1742):
										pass
									else:
										energy_authors_value_6_1743 = energy_authors_value_5_1742["document"]
										if not ("authors" in energy_authors_value_6_1743):
											pass
										else:
											energy_authors_value_7_1744 = energy_authors_value_6_1743["authors"]
											start_1745 = 0
											end_1746 = len(energy_authors_value_7_1744)
											for energy_authors_index_8_1747 in range(start_1745, end_1746):
												energy_authors_value_8_1748 = energy_authors_value_7_1744[energy_authors_index_8_1747]
												if True:
													writer_2.write_data_property("https://minmod.isi.edu/resource/authors", energy_authors_value_8_1748, None)
							
							# Retrieve value of data property: energy_description_document
							energy_description_document_value_0_1749 = resource_data_1["MineralSystem"]
							energy_description_document_index_1_1750 = energy_id_document_index_1_1687
							energy_description_document_value_1_1751 = energy_description_document_value_0_1749[energy_description_document_index_1_1750]
							if not ("energy" in energy_description_document_value_1_1751):
								pass
							else:
								energy_description_document_value_2_1752 = energy_description_document_value_1_1751["energy"]
								energy_description_document_index_3_1753 = energy_id_document_index_3_1692
								energy_description_document_value_3_1754 = energy_description_document_value_2_1752[energy_description_document_index_3_1753]
								if not ("supporting_references" in energy_description_document_value_3_1754):
									pass
								else:
									energy_description_document_value_4_1755 = energy_description_document_value_3_1754["supporting_references"]
									energy_description_document_index_5_1756 = energy_id_document_index_5_1697
									energy_description_document_value_5_1757 = energy_description_document_value_4_1755[energy_description_document_index_5_1756]
									if not ("document" in energy_description_document_value_5_1757):
										pass
									else:
										energy_description_document_value_6_1758 = energy_description_document_value_5_1757["document"]
										if not ("description" in energy_description_document_value_6_1758):
											pass
										else:
											energy_description_document_value_7_1759 = energy_description_document_value_6_1758["description"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/description", energy_description_document_value_7_1759, None)
							
							# Retrieve value of data property: energy_title_document
							energy_title_document_value_0_1760 = resource_data_1["MineralSystem"]
							energy_title_document_index_1_1761 = energy_id_document_index_1_1687
							energy_title_document_value_1_1762 = energy_title_document_value_0_1760[energy_title_document_index_1_1761]
							if not ("energy" in energy_title_document_value_1_1762):
								pass
							else:
								energy_title_document_value_2_1763 = energy_title_document_value_1_1762["energy"]
								energy_title_document_index_3_1764 = energy_id_document_index_3_1692
								energy_title_document_value_3_1765 = energy_title_document_value_2_1763[energy_title_document_index_3_1764]
								if not ("supporting_references" in energy_title_document_value_3_1765):
									pass
								else:
									energy_title_document_value_4_1766 = energy_title_document_value_3_1765["supporting_references"]
									energy_title_document_index_5_1767 = energy_id_document_index_5_1697
									energy_title_document_value_5_1768 = energy_title_document_value_4_1766[energy_title_document_index_5_1767]
									if not ("document" in energy_title_document_value_5_1768):
										pass
									else:
										energy_title_document_value_6_1769 = energy_title_document_value_5_1768["document"]
										if not ("title" in energy_title_document_value_6_1769):
											pass
										else:
											energy_title_document_value_7_1770 = energy_title_document_value_6_1769["title"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/title", energy_title_document_value_7_1770, None)
							
							# Retrieve value of data property: energy_volume
							energy_volume_value_0_1771 = resource_data_1["MineralSystem"]
							energy_volume_index_1_1772 = energy_id_document_index_1_1687
							energy_volume_value_1_1773 = energy_volume_value_0_1771[energy_volume_index_1_1772]
							if not ("energy" in energy_volume_value_1_1773):
								pass
							else:
								energy_volume_value_2_1774 = energy_volume_value_1_1773["energy"]
								energy_volume_index_3_1775 = energy_id_document_index_3_1692
								energy_volume_value_3_1776 = energy_volume_value_2_1774[energy_volume_index_3_1775]
								if not ("supporting_references" in energy_volume_value_3_1776):
									pass
								else:
									energy_volume_value_4_1777 = energy_volume_value_3_1776["supporting_references"]
									energy_volume_index_5_1778 = energy_id_document_index_5_1697
									energy_volume_value_5_1779 = energy_volume_value_4_1777[energy_volume_index_5_1778]
									if not ("document" in energy_volume_value_5_1779):
										pass
									else:
										energy_volume_value_6_1780 = energy_volume_value_5_1779["document"]
										if not ("volume" in energy_volume_value_6_1780):
											pass
										else:
											energy_volume_value_7_1781 = energy_volume_value_6_1780["volume"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/volume", energy_volume_value_7_1781, None)
							
							# Retrieve value of data property: energy_issue_document
							energy_issue_document_value_0_1782 = resource_data_1["MineralSystem"]
							energy_issue_document_index_1_1783 = energy_id_document_index_1_1687
							energy_issue_document_value_1_1784 = energy_issue_document_value_0_1782[energy_issue_document_index_1_1783]
							if not ("energy" in energy_issue_document_value_1_1784):
								pass
							else:
								energy_issue_document_value_2_1785 = energy_issue_document_value_1_1784["energy"]
								energy_issue_document_index_3_1786 = energy_id_document_index_3_1692
								energy_issue_document_value_3_1787 = energy_issue_document_value_2_1785[energy_issue_document_index_3_1786]
								if not ("supporting_references" in energy_issue_document_value_3_1787):
									pass
								else:
									energy_issue_document_value_4_1788 = energy_issue_document_value_3_1787["supporting_references"]
									energy_issue_document_index_5_1789 = energy_id_document_index_5_1697
									energy_issue_document_value_5_1790 = energy_issue_document_value_4_1788[energy_issue_document_index_5_1789]
									if not ("document" in energy_issue_document_value_5_1790):
										pass
									else:
										energy_issue_document_value_6_1791 = energy_issue_document_value_5_1790["document"]
										if not ("issue" in energy_issue_document_value_6_1791):
											pass
										else:
											energy_issue_document_value_7_1792 = energy_issue_document_value_6_1791["issue"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/issue", energy_issue_document_value_7_1792, None)
							
							# Retrieve value of data property: energy_month_document
							energy_month_document_value_0_1793 = resource_data_1["MineralSystem"]
							energy_month_document_index_1_1794 = energy_id_document_index_1_1687
							energy_month_document_value_1_1795 = energy_month_document_value_0_1793[energy_month_document_index_1_1794]
							if not ("energy" in energy_month_document_value_1_1795):
								pass
							else:
								energy_month_document_value_2_1796 = energy_month_document_value_1_1795["energy"]
								energy_month_document_index_3_1797 = energy_id_document_index_3_1692
								energy_month_document_value_3_1798 = energy_month_document_value_2_1796[energy_month_document_index_3_1797]
								if not ("supporting_references" in energy_month_document_value_3_1798):
									pass
								else:
									energy_month_document_value_4_1799 = energy_month_document_value_3_1798["supporting_references"]
									energy_month_document_index_5_1800 = energy_id_document_index_5_1697
									energy_month_document_value_5_1801 = energy_month_document_value_4_1799[energy_month_document_index_5_1800]
									if not ("document" in energy_month_document_value_5_1801):
										pass
									else:
										energy_month_document_value_6_1802 = energy_month_document_value_5_1801["document"]
										if not ("month" in energy_month_document_value_6_1802):
											pass
										else:
											energy_month_document_value_7_1803 = energy_month_document_value_6_1802["month"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/month", energy_month_document_value_7_1803, None)
							
							# Retrieve value of data property: energy_year_document
							energy_year_document_value_0_1804 = resource_data_1["MineralSystem"]
							energy_year_document_index_1_1805 = energy_id_document_index_1_1687
							energy_year_document_value_1_1806 = energy_year_document_value_0_1804[energy_year_document_index_1_1805]
							if not ("energy" in energy_year_document_value_1_1806):
								pass
							else:
								energy_year_document_value_2_1807 = energy_year_document_value_1_1806["energy"]
								energy_year_document_index_3_1808 = energy_id_document_index_3_1692
								energy_year_document_value_3_1809 = energy_year_document_value_2_1807[energy_year_document_index_3_1808]
								if not ("supporting_references" in energy_year_document_value_3_1809):
									pass
								else:
									energy_year_document_value_4_1810 = energy_year_document_value_3_1809["supporting_references"]
									energy_year_document_index_5_1811 = energy_id_document_index_5_1697
									energy_year_document_value_5_1812 = energy_year_document_value_4_1810[energy_year_document_index_5_1811]
									if not ("document" in energy_year_document_value_5_1812):
										pass
									else:
										energy_year_document_value_6_1813 = energy_year_document_value_5_1812["document"]
										if not ("year" in energy_year_document_value_6_1813):
											pass
										else:
											energy_year_document_value_7_1814 = energy_year_document_value_6_1813["year"]
											if True:
												writer_2.write_data_property("https://minmod.isi.edu/resource/year", energy_year_document_value_7_1814, None)
							
							writer_2.end_record()
	
	# Transform records of class mndr:BoundingBox:5
	energy_x_min_value_0_1815 = resource_data_1["MineralSystem"]
	start_1816 = 0
	end_1817 = len(energy_x_min_value_0_1815)
	for energy_x_min_index_1_1818 in range(start_1816, end_1817):
		energy_x_min_value_1_1819 = energy_x_min_value_0_1815[energy_x_min_index_1_1818]
		if not ("energy" in energy_x_min_value_1_1819):
			continue
		else:
			energy_x_min_value_2_1820 = energy_x_min_value_1_1819["energy"]
			start_1821 = 0
			end_1822 = len(energy_x_min_value_2_1820)
			for energy_x_min_index_3_1823 in range(start_1821, end_1822):
				energy_x_min_value_3_1824 = energy_x_min_value_2_1820[energy_x_min_index_3_1823]
				if not ("supporting_references" in energy_x_min_value_3_1824):
					continue
				else:
					energy_x_min_value_4_1825 = energy_x_min_value_3_1824["supporting_references"]
					start_1826 = 0
					end_1827 = len(energy_x_min_value_4_1825)
					for energy_x_min_index_5_1828 in range(start_1826, end_1827):
						energy_x_min_value_5_1829 = energy_x_min_value_4_1825[energy_x_min_index_5_1828]
						if not ("page_info" in energy_x_min_value_5_1829):
							continue
						else:
							energy_x_min_value_6_1830 = energy_x_min_value_5_1829["page_info"]
							start_1831 = 0
							end_1832 = len(energy_x_min_value_6_1830)
							for energy_x_min_index_7_1833 in range(start_1831, end_1832):
								energy_x_min_value_7_1834 = energy_x_min_value_6_1830[energy_x_min_index_7_1833]
								if not ("bounding_box" in energy_x_min_value_7_1834):
									continue
								else:
									energy_x_min_value_8_1835 = energy_x_min_value_7_1834["bounding_box"]
									if not ("x_min" in energy_x_min_value_8_1835):
										continue
									else:
										energy_x_min_value_9_1836 = energy_x_min_value_8_1835["x_min"]
										writer_2.begin_record("https://minmod.isi.edu/resource/BoundingBox", (108, energy_x_min_index_1_1818, energy_x_min_index_3_1823, energy_x_min_index_5_1828, energy_x_min_index_7_1833), True, False)
										
										# Retrieve value of data property: energy_x_min
										if True:
											writer_2.write_data_property("https://minmod.isi.edu/resource/x_min", energy_x_min_value_9_1836, None)
										
										# Retrieve value of data property: energy_x_max
										energy_x_max_value_0_1837 = resource_data_1["MineralSystem"]
										energy_x_max_index_1_1838 = energy_x_min_index_1_1818
										energy_x_max_value_1_1839 = energy_x_max_value_0_1837[energy_x_max_index_1_1838]
										if not ("energy" in energy_x_max_value_1_1839):
											pass
										else:
											energy_x_max_value_2_1840 = energy_x_max_value_1_1839["energy"]
											energy_x_max_index_3_1841 = energy_x_min_index_3_1823
											energy_x_max_value_3_1842 = energy_x_max_value_2_1840[energy_x_max_index_3_1841]
											if not ("supporting_references" in energy_x_max_value_3_1842):
												pass
											else:
												energy_x_max_value_4_1843 = energy_x_max_value_3_1842["supporting_references"]
												energy_x_max_index_5_1844 = energy_x_min_index_5_1828
												energy_x_max_value_5_1845 = energy_x_max_value_4_1843[energy_x_max_index_5_1844]
												if not ("page_info" in energy_x_max_value_5_1845):
													pass
												else:
													energy_x_max_value_6_1846 = energy_x_max_value_5_1845["page_info"]
													energy_x_max_index_7_1847 = energy_x_min_index_7_1833
													energy_x_max_value_7_1848 = energy_x_max_value_6_1846[energy_x_max_index_7_1847]
													if not ("bounding_box" in energy_x_max_value_7_1848):
														pass
													else:
														energy_x_max_value_8_1849 = energy_x_max_value_7_1848["bounding_box"]
														if not ("x_max" in energy_x_max_value_8_1849):
															pass
														else:
															energy_x_max_value_9_1850 = energy_x_max_value_8_1849["x_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/x_max", energy_x_max_value_9_1850, None)
										
										# Retrieve value of data property: energy_y_min
										energy_y_min_value_0_1851 = resource_data_1["MineralSystem"]
										energy_y_min_index_1_1852 = energy_x_min_index_1_1818
										energy_y_min_value_1_1853 = energy_y_min_value_0_1851[energy_y_min_index_1_1852]
										if not ("energy" in energy_y_min_value_1_1853):
											pass
										else:
											energy_y_min_value_2_1854 = energy_y_min_value_1_1853["energy"]
											energy_y_min_index_3_1855 = energy_x_min_index_3_1823
											energy_y_min_value_3_1856 = energy_y_min_value_2_1854[energy_y_min_index_3_1855]
											if not ("supporting_references" in energy_y_min_value_3_1856):
												pass
											else:
												energy_y_min_value_4_1857 = energy_y_min_value_3_1856["supporting_references"]
												energy_y_min_index_5_1858 = energy_x_min_index_5_1828
												energy_y_min_value_5_1859 = energy_y_min_value_4_1857[energy_y_min_index_5_1858]
												if not ("page_info" in energy_y_min_value_5_1859):
													pass
												else:
													energy_y_min_value_6_1860 = energy_y_min_value_5_1859["page_info"]
													energy_y_min_index_7_1861 = energy_x_min_index_7_1833
													energy_y_min_value_7_1862 = energy_y_min_value_6_1860[energy_y_min_index_7_1861]
													if not ("bounding_box" in energy_y_min_value_7_1862):
														pass
													else:
														energy_y_min_value_8_1863 = energy_y_min_value_7_1862["bounding_box"]
														if not ("y_min" in energy_y_min_value_8_1863):
															pass
														else:
															energy_y_min_value_9_1864 = energy_y_min_value_8_1863["y_min"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_min", energy_y_min_value_9_1864, None)
										
										# Retrieve value of data property: energy_y_max
										energy_y_max_value_0_1865 = resource_data_1["MineralSystem"]
										energy_y_max_index_1_1866 = energy_x_min_index_1_1818
										energy_y_max_value_1_1867 = energy_y_max_value_0_1865[energy_y_max_index_1_1866]
										if not ("energy" in energy_y_max_value_1_1867):
											pass
										else:
											energy_y_max_value_2_1868 = energy_y_max_value_1_1867["energy"]
											energy_y_max_index_3_1869 = energy_x_min_index_3_1823
											energy_y_max_value_3_1870 = energy_y_max_value_2_1868[energy_y_max_index_3_1869]
											if not ("supporting_references" in energy_y_max_value_3_1870):
												pass
											else:
												energy_y_max_value_4_1871 = energy_y_max_value_3_1870["supporting_references"]
												energy_y_max_index_5_1872 = energy_x_min_index_5_1828
												energy_y_max_value_5_1873 = energy_y_max_value_4_1871[energy_y_max_index_5_1872]
												if not ("page_info" in energy_y_max_value_5_1873):
													pass
												else:
													energy_y_max_value_6_1874 = energy_y_max_value_5_1873["page_info"]
													energy_y_max_index_7_1875 = energy_x_min_index_7_1833
													energy_y_max_value_7_1876 = energy_y_max_value_6_1874[energy_y_max_index_7_1875]
													if not ("bounding_box" in energy_y_max_value_7_1876):
														pass
													else:
														energy_y_max_value_8_1877 = energy_y_max_value_7_1876["bounding_box"]
														if not ("y_max" in energy_y_max_value_8_1877):
															pass
														else:
															energy_y_max_value_9_1878 = energy_y_max_value_8_1877["y_max"]
															if True:
																writer_2.write_data_property("https://minmod.isi.edu/resource/y_max", energy_y_max_value_9_1878, None)
										
										writer_2.end_record()
	
	# Transform records of class mndr:PageInfo:5
	energy_page_value_0_1879 = resource_data_1["MineralSystem"]
	start_1880 = 0
	end_1881 = len(energy_page_value_0_1879)
	for energy_page_index_1_1882 in range(start_1880, end_1881):
		energy_page_value_1_1883 = energy_page_value_0_1879[energy_page_index_1_1882]
		if not ("energy" in energy_page_value_1_1883):
			continue
		else:
			energy_page_value_2_1884 = energy_page_value_1_1883["energy"]
			start_1885 = 0
			end_1886 = len(energy_page_value_2_1884)
			for energy_page_index_3_1887 in range(start_1885, end_1886):
				energy_page_value_3_1888 = energy_page_value_2_1884[energy_page_index_3_1887]
				if not ("supporting_references" in energy_page_value_3_1888):
					continue
				else:
					energy_page_value_4_1889 = energy_page_value_3_1888["supporting_references"]
					start_1890 = 0
					end_1891 = len(energy_page_value_4_1889)
					for energy_page_index_5_1892 in range(start_1890, end_1891):
						energy_page_value_5_1893 = energy_page_value_4_1889[energy_page_index_5_1892]
						if not ("page_info" in energy_page_value_5_1893):
							continue
						else:
							energy_page_value_6_1894 = energy_page_value_5_1893["page_info"]
							start_1895 = 0
							end_1896 = len(energy_page_value_6_1894)
							for energy_page_index_7_1897 in range(start_1895, end_1896):
								energy_page_value_7_1898 = energy_page_value_6_1894[energy_page_index_7_1897]
								if not ("page" in energy_page_value_7_1898):
									continue
								else:
									energy_page_value_8_1899 = energy_page_value_7_1898["page"]
									writer_2.begin_record("https://minmod.isi.edu/resource/PageInfo", (106, energy_page_index_1_1882, energy_page_index_3_1887, energy_page_index_5_1892, energy_page_index_7_1897), True, False)
									
									# Retrieve value of data property: energy_page
									if True:
										writer_2.write_data_property("https://minmod.isi.edu/resource/page", energy_page_value_8_1899, None)
									
									# Retrieve value of object property: energy_x_min
									energy_x_min_value_0_1900 = resource_data_1["MineralSystem"]
									energy_x_min_index_1_1901 = energy_page_index_1_1882
									energy_x_min_value_1_1902 = energy_x_min_value_0_1900[energy_x_min_index_1_1901]
									if not ("energy" in energy_x_min_value_1_1902):
										pass
									else:
										energy_x_min_value_2_1903 = energy_x_min_value_1_1902["energy"]
										energy_x_min_index_3_1904 = energy_page_index_3_1887
										energy_x_min_value_3_1905 = energy_x_min_value_2_1903[energy_x_min_index_3_1904]
										if not ("supporting_references" in energy_x_min_value_3_1905):
											pass
										else:
											energy_x_min_value_4_1906 = energy_x_min_value_3_1905["supporting_references"]
											energy_x_min_index_5_1907 = energy_page_index_5_1892
											energy_x_min_value_5_1908 = energy_x_min_value_4_1906[energy_x_min_index_5_1907]
											if not ("page_info" in energy_x_min_value_5_1908):
												pass
											else:
												energy_x_min_value_6_1909 = energy_x_min_value_5_1908["page_info"]
												energy_x_min_index_7_1910 = energy_page_index_7_1897
												energy_x_min_value_7_1911 = energy_x_min_value_6_1909[energy_x_min_index_7_1910]
												if not ("bounding_box" in energy_x_min_value_7_1911):
													pass
												else:
													energy_x_min_value_8_1912 = energy_x_min_value_7_1911["bounding_box"]
													if not ("x_min" in energy_x_min_value_8_1912):
														pass
													else:
														energy_x_min_value_9_1913 = energy_x_min_value_8_1912["x_min"]
														if writer_2.has_written_record((108, energy_x_min_index_1_1901, energy_x_min_index_3_1904, energy_x_min_index_5_1907, energy_x_min_index_7_1910)):
															writer_2.write_object_property("https://minmod.isi.edu/resource/bounding_box", (108, energy_x_min_index_1_1901, energy_x_min_index_3_1904, energy_x_min_index_5_1907, energy_x_min_index_7_1910), True, True, False)
									
									writer_2.end_record()
	
	# Transform records of class mndr:Reference:5
	energy_id_document_value_0_1914 = resource_data_1["MineralSystem"]
	start_1915 = 0
	end_1916 = len(energy_id_document_value_0_1914)
	for energy_id_document_index_1_1917 in range(start_1915, end_1916):
		energy_id_document_value_1_1918 = energy_id_document_value_0_1914[energy_id_document_index_1_1917]
		if not ("energy" in energy_id_document_value_1_1918):
			continue
		else:
			energy_id_document_value_2_1919 = energy_id_document_value_1_1918["energy"]
			start_1920 = 0
			end_1921 = len(energy_id_document_value_2_1919)
			for energy_id_document_index_3_1922 in range(start_1920, end_1921):
				energy_id_document_value_3_1923 = energy_id_document_value_2_1919[energy_id_document_index_3_1922]
				if not ("supporting_references" in energy_id_document_value_3_1923):
					continue
				else:
					energy_id_document_value_4_1924 = energy_id_document_value_3_1923["supporting_references"]
					start_1925 = 0
					end_1926 = len(energy_id_document_value_4_1924)
					for energy_id_document_index_5_1927 in range(start_1925, end_1926):
						energy_id_document_value_5_1928 = energy_id_document_value_4_1924[energy_id_document_index_5_1927]
						if not ("document" in energy_id_document_value_5_1928):
							continue
						else:
							energy_id_document_value_6_1929 = energy_id_document_value_5_1928["document"]
							energy_id_document_value_7_1930 = energy_id_document_value_6_1929["id"]
							writer_2.begin_record("https://minmod.isi.edu/resource/Reference", (96, energy_id_document_index_1_1917, energy_id_document_index_3_1922, energy_id_document_index_5_1927), True, False)
							
							# Retrieve value of data property: energy_id_document
							if True:
								writer_2.write_data_property("https://minmod.isi.edu/resource/document_id", energy_id_document_value_7_1930, None)
							
							# Retrieve value of object property: energy_id_document
							if writer_2.has_written_record(energy_id_document_value_7_1930):
								writer_2.write_object_property("https://minmod.isi.edu/resource/document", energy_id_document_value_7_1930, True, False, False)
							
							# Retrieve value of object property: energy_page
							energy_page_value_0_1931 = resource_data_1["MineralSystem"]
							energy_page_index_1_1932 = energy_id_document_index_1_1917
							energy_page_value_1_1933 = energy_page_value_0_1931[energy_page_index_1_1932]
							if not ("energy" in energy_page_value_1_1933):
								pass
							else:
								energy_page_value_2_1934 = energy_page_value_1_1933["energy"]
								energy_page_index_3_1935 = energy_id_document_index_3_1922
								energy_page_value_3_1936 = energy_page_value_2_1934[energy_page_index_3_1935]
								if not ("supporting_references" in energy_page_value_3_1936):
									pass
								else:
									energy_page_value_4_1937 = energy_page_value_3_1936["supporting_references"]
									energy_page_index_5_1938 = energy_id_document_index_5_1927
									energy_page_value_5_1939 = energy_page_value_4_1937[energy_page_index_5_1938]
									if not ("page_info" in energy_page_value_5_1939):
										pass
									else:
										energy_page_value_6_1940 = energy_page_value_5_1939["page_info"]
										start_1941 = 0
										end_1942 = len(energy_page_value_6_1940)
										for energy_page_index_7_1943 in range(start_1941, end_1942):
											energy_page_value_7_1944 = energy_page_value_6_1940[energy_page_index_7_1943]
											if not ("page" in energy_page_value_7_1944):
												pass
											else:
												energy_page_value_8_1945 = energy_page_value_7_1944["page"]
												if writer_2.has_written_record((106, energy_page_index_1_1932, energy_page_index_3_1935, energy_page_index_5_1938, energy_page_index_7_1943)):
													writer_2.write_object_property("https://minmod.isi.edu/resource/page_info", (106, energy_page_index_1_1932, energy_page_index_3_1935, energy_page_index_5_1938, energy_page_index_7_1943), True, True, False)
							
							writer_2.end_record()
	
	# Transform records of class mndr:MappableCriteria:5
	energy_criteria_value_0_1946 = resource_data_1["MineralSystem"]
	start_1947 = 0
	end_1948 = len(energy_criteria_value_0_1946)
	for energy_criteria_index_1_1949 in range(start_1947, end_1948):
		energy_criteria_value_1_1950 = energy_criteria_value_0_1946[energy_criteria_index_1_1949]
		if not ("energy" in energy_criteria_value_1_1950):
			continue
		else:
			energy_criteria_value_2_1951 = energy_criteria_value_1_1950["energy"]
			start_1952 = 0
			end_1953 = len(energy_criteria_value_2_1951)
			for energy_criteria_index_3_1954 in range(start_1952, end_1953):
				energy_criteria_value_3_1955 = energy_criteria_value_2_1951[energy_criteria_index_3_1954]
				energy_criteria_value_4_1956 = energy_criteria_value_3_1955["criteria"]
				writer_2.begin_record("https://minmod.isi.edu/resource/MappableCriteria", (90, energy_criteria_index_1_1949, energy_criteria_index_3_1954), True, False)
				
				# Retrieve value of data property: energy_criteria
				if True:
					writer_2.write_data_property("https://minmod.isi.edu/resource/criteria", energy_criteria_value_4_1956, None)
				
				# Retrieve value of data property: energy_theoretical
				energy_theoretical_value_0_1957 = resource_data_1["MineralSystem"]
				energy_theoretical_index_1_1958 = energy_criteria_index_1_1949
				energy_theoretical_value_1_1959 = energy_theoretical_value_0_1957[energy_theoretical_index_1_1958]
				if not ("energy" in energy_theoretical_value_1_1959):
					pass
				else:
					energy_theoretical_value_2_1960 = energy_theoretical_value_1_1959["energy"]
					energy_theoretical_index_3_1961 = energy_criteria_index_3_1954
					energy_theoretical_value_3_1962 = energy_theoretical_value_2_1960[energy_theoretical_index_3_1961]
					if not ("theoretical" in energy_theoretical_value_3_1962):
						pass
					else:
						energy_theoretical_value_4_1963 = energy_theoretical_value_3_1962["theoretical"]
						if True:
							writer_2.write_data_property("https://minmod.isi.edu/resource/theoretical", energy_theoretical_value_4_1963, None)
				
				# Retrieve value of object property: energy_potential_dataset_name
				energy_potential_dataset_name_value_0_1964 = resource_data_1["MineralSystem"]
				energy_potential_dataset_name_index_1_1965 = energy_criteria_index_1_1949
				energy_potential_dataset_name_value_1_1966 = energy_potential_dataset_name_value_0_1964[energy_potential_dataset_name_index_1_1965]
				if not ("energy" in energy_potential_dataset_name_value_1_1966):
					pass
				else:
					energy_potential_dataset_name_value_2_1967 = energy_potential_dataset_name_value_1_1966["energy"]
					energy_potential_dataset_name_index_3_1968 = energy_criteria_index_3_1954
					energy_potential_dataset_name_value_3_1969 = energy_potential_dataset_name_value_2_1967[energy_potential_dataset_name_index_3_1968]
					if not ("potential_dataset" in energy_potential_dataset_name_value_3_1969):
						pass
					else:
						energy_potential_dataset_name_value_4_1970 = energy_potential_dataset_name_value_3_1969["potential_dataset"]
						start_1971 = 0
						end_1972 = len(energy_potential_dataset_name_value_4_1970)
						for energy_potential_dataset_name_index_5_1973 in range(start_1971, end_1972):
							energy_potential_dataset_name_value_5_1974 = energy_potential_dataset_name_value_4_1970[energy_potential_dataset_name_index_5_1973]
							energy_potential_dataset_name_value_6_1975 = energy_potential_dataset_name_value_5_1974["name"]
							if writer_2.has_written_record((92, energy_potential_dataset_name_index_1_1965, energy_potential_dataset_name_index_3_1968, energy_potential_dataset_name_index_5_1973)):
								writer_2.write_object_property("https://minmod.isi.edu/resource/potential_dataset", (92, energy_potential_dataset_name_index_1_1965, energy_potential_dataset_name_index_3_1968, energy_potential_dataset_name_index_5_1973), True, True, False)
				
				# Retrieve value of object property: energy_id_document
				energy_id_document_value_0_1976 = resource_data_1["MineralSystem"]
				energy_id_document_index_1_1977 = energy_criteria_index_1_1949
				energy_id_document_value_1_1978 = energy_id_document_value_0_1976[energy_id_document_index_1_1977]
				if not ("energy" in energy_id_document_value_1_1978):
					pass
				else:
					energy_id_document_value_2_1979 = energy_id_document_value_1_1978["energy"]
					energy_id_document_index_3_1980 = energy_criteria_index_3_1954
					energy_id_document_value_3_1981 = energy_id_document_value_2_1979[energy_id_document_index_3_1980]
					if not ("supporting_references" in energy_id_document_value_3_1981):
						pass
					else:
						energy_id_document_value_4_1982 = energy_id_document_value_3_1981["supporting_references"]
						start_1983 = 0
						end_1984 = len(energy_id_document_value_4_1982)
						for energy_id_document_index_5_1985 in range(start_1983, end_1984):
							energy_id_document_value_5_1986 = energy_id_document_value_4_1982[energy_id_document_index_5_1985]
							if not ("document" in energy_id_document_value_5_1986):
								pass
							else:
								energy_id_document_value_6_1987 = energy_id_document_value_5_1986["document"]
								energy_id_document_value_7_1988 = energy_id_document_value_6_1987["id"]
								if writer_2.has_written_record((96, energy_id_document_index_1_1977, energy_id_document_index_3_1980, energy_id_document_index_5_1985)):
									writer_2.write_object_property("https://minmod.isi.edu/resource/supporting_references", (96, energy_id_document_index_1_1977, energy_id_document_index_3_1980, energy_id_document_index_5_1985), True, True, False)
				
				writer_2.end_record()
	
	# Transform records of class mndr:MineralSystem:1
	ms_id_value_0_1989 = resource_data_1["MineralSystem"]
	start_1990 = 0
	end_1991 = len(ms_id_value_0_1989)
	for ms_id_index_1_1992 in range(start_1990, end_1991):
		ms_id_value_1_1993 = ms_id_value_0_1989[ms_id_index_1_1992]
		ms_id_value_2_1994 = ms_id_value_1_1993["id"]
		writer_2.begin_record("https://minmod.isi.edu/resource/MineralSystem", ms_id_value_2_1994, False, False)
		
		# Retrieve value of data property: ms_id
		writer_2.write_data_property("https://minmod.isi.edu/resource/id", ms_id_value_2_1994, None)
		
		# Retrieve value of data property: deposit_type
		deposit_type_value_0_1995 = resource_data_1["MineralSystem"]
		deposit_type_index_1_1996 = ms_id_index_1_1992
		deposit_type_value_1_1997 = deposit_type_value_0_1995[deposit_type_index_1_1996]
		deposit_type_value_2_1998 = deposit_type_value_1_1997["deposit_type"]
		start_1999 = 0
		end_2000 = len(deposit_type_value_2_1998)
		for deposit_type_index_3_2001 in range(start_1999, end_2000):
			deposit_type_value_3_2002 = deposit_type_value_2_1998[deposit_type_index_3_2001]
			writer_2.write_data_property("https://minmod.isi.edu/resource/deposit_type", deposit_type_value_3_2002, "https://purl.org/drepr/1.0/uri")
		
		# Retrieve value of object property: pathway_criteria
		pathway_criteria_value_0_2003 = resource_data_1["MineralSystem"]
		pathway_criteria_index_1_2004 = ms_id_index_1_1992
		pathway_criteria_value_1_2005 = pathway_criteria_value_0_2003[pathway_criteria_index_1_2004]
		pathway_criteria_value_2_2006 = pathway_criteria_value_1_2005["pathway"]
		start_2007 = 0
		end_2008 = len(pathway_criteria_value_2_2006)
		for pathway_criteria_index_3_2009 in range(start_2007, end_2008):
			pathway_criteria_value_3_2010 = pathway_criteria_value_2_2006[pathway_criteria_index_3_2009]
			pathway_criteria_value_4_2011 = pathway_criteria_value_3_2010["criteria"]
			writer_2.write_object_property("https://minmod.isi.edu/resource/pathway", (24, pathway_criteria_index_1_2004, pathway_criteria_index_3_2009), False, True, False)
		
		# Retrieve value of object property: trap_criteria
		trap_criteria_value_0_2012 = resource_data_1["MineralSystem"]
		trap_criteria_index_1_2013 = ms_id_index_1_1992
		trap_criteria_value_1_2014 = trap_criteria_value_0_2012[trap_criteria_index_1_2013]
		if not ("trap" in trap_criteria_value_1_2014):
			pass
		else:
			trap_criteria_value_2_2015 = trap_criteria_value_1_2014["trap"]
			start_2016 = 0
			end_2017 = len(trap_criteria_value_2_2015)
			for trap_criteria_index_3_2018 in range(start_2016, end_2017):
				trap_criteria_value_3_2019 = trap_criteria_value_2_2015[trap_criteria_index_3_2018]
				trap_criteria_value_4_2020 = trap_criteria_value_3_2019["criteria"]
				if writer_2.has_written_record((46, trap_criteria_index_1_2013, trap_criteria_index_3_2018)):
					writer_2.write_object_property("https://minmod.isi.edu/resource/trap", (46, trap_criteria_index_1_2013, trap_criteria_index_3_2018), False, True, False)
		
		# Retrieve value of object property: source_criteria
		source_criteria_value_0_2021 = resource_data_1["MineralSystem"]
		source_criteria_index_1_2022 = ms_id_index_1_1992
		source_criteria_value_1_2023 = source_criteria_value_0_2021[source_criteria_index_1_2022]
		source_criteria_value_2_2024 = source_criteria_value_1_2023["source"]
		start_2025 = 0
		end_2026 = len(source_criteria_value_2_2024)
		for source_criteria_index_3_2027 in range(start_2025, end_2026):
			source_criteria_value_3_2028 = source_criteria_value_2_2024[source_criteria_index_3_2027]
			source_criteria_value_4_2029 = source_criteria_value_3_2028["criteria"]
			writer_2.write_object_property("https://minmod.isi.edu/resource/source", (2, source_criteria_index_1_2022, source_criteria_index_3_2027), False, True, False)
		
		# Retrieve value of object property: preservation_criteria
		preservation_criteria_value_0_2030 = resource_data_1["MineralSystem"]
		preservation_criteria_index_1_2031 = ms_id_index_1_1992
		preservation_criteria_value_1_2032 = preservation_criteria_value_0_2030[preservation_criteria_index_1_2031]
		if not ("preservation" in preservation_criteria_value_1_2032):
			pass
		else:
			preservation_criteria_value_2_2033 = preservation_criteria_value_1_2032["preservation"]
			start_2034 = 0
			end_2035 = len(preservation_criteria_value_2_2033)
			for preservation_criteria_index_3_2036 in range(start_2034, end_2035):
				preservation_criteria_value_3_2037 = preservation_criteria_value_2_2033[preservation_criteria_index_3_2036]
				preservation_criteria_value_4_2038 = preservation_criteria_value_3_2037["criteria"]
				if writer_2.has_written_record((68, preservation_criteria_index_1_2031, preservation_criteria_index_3_2036)):
					writer_2.write_object_property("https://minmod.isi.edu/resource/prservation", (68, preservation_criteria_index_1_2031, preservation_criteria_index_3_2036), False, True, False)
		
		# Retrieve value of object property: outflow_criteria
		outflow_criteria_value_0_2039 = resource_data_1["MineralSystem"]
		outflow_criteria_index_1_2040 = ms_id_index_1_1992
		outflow_criteria_value_1_2041 = outflow_criteria_value_0_2039[outflow_criteria_index_1_2040]
		if not ("outflow" in outflow_criteria_value_1_2041):
			pass
		else:
			outflow_criteria_value_2_2042 = outflow_criteria_value_1_2041["outflow"]
			start_2043 = 0
			end_2044 = len(outflow_criteria_value_2_2042)
			for outflow_criteria_index_3_2045 in range(start_2043, end_2044):
				outflow_criteria_value_3_2046 = outflow_criteria_value_2_2042[outflow_criteria_index_3_2045]
				outflow_criteria_value_4_2047 = outflow_criteria_value_3_2046["criteria"]
				if writer_2.has_written_record((112, outflow_criteria_index_1_2040, outflow_criteria_index_3_2045)):
					writer_2.write_object_property("https://minmod.isi.edu/resource/outflow", (112, outflow_criteria_index_1_2040, outflow_criteria_index_3_2045), False, True, False)
		
		# Retrieve value of object property: energy_criteria
		energy_criteria_value_0_2048 = resource_data_1["MineralSystem"]
		energy_criteria_index_1_2049 = ms_id_index_1_1992
		energy_criteria_value_1_2050 = energy_criteria_value_0_2048[energy_criteria_index_1_2049]
		if not ("energy" in energy_criteria_value_1_2050):
			pass
		else:
			energy_criteria_value_2_2051 = energy_criteria_value_1_2050["energy"]
			start_2052 = 0
			end_2053 = len(energy_criteria_value_2_2051)
			for energy_criteria_index_3_2054 in range(start_2052, end_2053):
				energy_criteria_value_3_2055 = energy_criteria_value_2_2051[energy_criteria_index_3_2054]
				energy_criteria_value_4_2056 = energy_criteria_value_3_2055["criteria"]
				if writer_2.has_written_record((90, energy_criteria_index_1_2049, energy_criteria_index_3_2054)):
					writer_2.write_object_property("https://minmod.isi.edu/resource/energy", (90, energy_criteria_index_1_2049, energy_criteria_index_3_2054), False, True, False)
		
		writer_2.end_record()
	
	output_2057 = writer_2.write_to_string()
	return output_2057

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))