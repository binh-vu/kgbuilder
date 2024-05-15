from drepr.readers.prelude import read_source_json
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_json(resource_0)
	
	name_mineral_site_missing_values_2 = {-1}
	mineral_inven_missing_values_3 = {-1}
	id_deposit_type_candidate_missing_values_4 = {-1}
	deposit_type_name_missing_values_5 = {-1}
	deposit_type_source_missing_values_6 = {-1}
	deposit_type_confidence_missing_values_7 = {-1}
	deposit_type_normalized_uri_missing_values_8 = {""}
	geology_info_missing_values_9 = {-1}
	location_info_location_missing_values_10 = {-1}
	location_info_country_missing_values_11 = {-1}
	location_info_state_missing_values_12 = {-1}
	location_info_location_source_record_id_missing_values_13 = {-1}
	location_info_location_source_missing_values_14 = {-1}
	location_info_crs_missing_values_15 = {-1}
	geology_info_age_missing_values_16 = {-1}
	geology_info_unit_name_missing_values_17 = {-1}
	geology_info_description_missing_values_18 = {-1}
	geology_info_lithology_missing_values_19 = {-1}
	geology_info_process_missing_values_20 = {-1}
	geology_info_environment_missing_values_21 = {-1}
	geology_info_comments_missing_values_22 = {-1}
	commodity_missing_values_23 = {""}
	observed_commodity_missing_values_24 = {-1}
	ore_missing_values_25 = {-1}
	ore_value_missing_values_26 = {-1}
	grade_value_missing_values_27 = {-1}
	cutoff_grade_value_missing_values_28 = {-1}
	cutoff_grade_unit_missing_values_29 = {""}
	ore_unit_missing_values_30 = {""}
	grade_unit_missing_values_31 = {""}
	category_missing_values_32 = {-1}
	date_missing_values_33 = {-1}
	zone_missing_values_34 = {-1}
	id_reference_missing_values_35 = {-1}
	issue_document_missing_values_36 = {-1}
	id_document_missing_values_37 = {-1}
	id_document_ref_missing_values_38 = {-1}
	uri_document_missing_values_39 = {-1}
	doi_missing_values_40 = {-1}
	volume_missing_values_41 = {-1}
	year_document_missing_values_42 = {-1}
	month_document_missing_values_43 = {-1}
	journal_missing_values_44 = {-1}
	description_document_missing_values_45 = {-1}
	title_document_missing_values_46 = {-1}
	page_info_array_missing_values_47 = {-1}
	page_info_missing_values_48 = {-1}
	bounding_box_missing_values_49 = {-1}
	x_min_missing_values_50 = {-1}
	x_max_missing_values_51 = {-1}
	y_min_missing_values_52 = {-1}
	y_max_missing_values_53 = {-1}
	page_missing_values_54 = {-1}
	writer_55 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "geokb": "https://geokb.wikibase.cloud/entity/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "xsd": "http://www.w3.org/2001/XMLSchema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "geo": "http://www.opengis.net/ont/geosparql#", "gkbi": "https://geokb.wikibase.cloud/entity/", "gkbp": "https://geokb.wikibase.cloud/wiki/Property/"})
	
	# Transform records of class mndr:DepositTypeCandidate:1
	id_deposit_type_candidate_value_0_56 = resource_data_1["MineralSite"]
	start_57 = 0
	end_58 = len(id_deposit_type_candidate_value_0_56)
	for id_deposit_type_candidate_index_1_59 in range(start_57, end_58):
		id_deposit_type_candidate_value_1_60 = id_deposit_type_candidate_value_0_56[id_deposit_type_candidate_index_1_59]
		if not ("deposit_type_candidate" in id_deposit_type_candidate_value_1_60):
			continue
		else:
			id_deposit_type_candidate_value_2_61 = id_deposit_type_candidate_value_1_60["deposit_type_candidate"]
			start_62 = 0
			end_63 = len(id_deposit_type_candidate_value_2_61)
			for id_deposit_type_candidate_index_3_64 in range(start_62, end_63):
				id_deposit_type_candidate_value_3_65 = id_deposit_type_candidate_value_2_61[id_deposit_type_candidate_index_3_64]
				if not ("id" in id_deposit_type_candidate_value_3_65):
					continue
				else:
					id_deposit_type_candidate_value_4_66 = id_deposit_type_candidate_value_3_65["id"]
					if id_deposit_type_candidate_value_4_66 in id_deposit_type_candidate_missing_values_4:
						continue
					writer_55.begin_record("https://minmod.isi.edu/resource/DepositTypeCandidate", id_deposit_type_candidate_value_4_66, False, False)
					
					# Retrieve value of data property: deposit_type_name
					deposit_type_name_value_0_67 = resource_data_1["MineralSite"]
					deposit_type_name_index_1_68 = id_deposit_type_candidate_index_1_59
					deposit_type_name_value_1_69 = deposit_type_name_value_0_67[deposit_type_name_index_1_68]
					if not ("deposit_type_candidate" in deposit_type_name_value_1_69):
						pass
					else:
						deposit_type_name_value_2_70 = deposit_type_name_value_1_69["deposit_type_candidate"]
						deposit_type_name_index_3_71 = id_deposit_type_candidate_index_3_64
						deposit_type_name_value_3_72 = deposit_type_name_value_2_70[deposit_type_name_index_3_71]
						if not ("observed_name" in deposit_type_name_value_3_72):
							pass
						else:
							deposit_type_name_value_4_73 = deposit_type_name_value_3_72["observed_name"]
							if not (deposit_type_name_value_4_73 in deposit_type_name_missing_values_5):
								writer_55.write_data_property("https://minmod.isi.edu/resource/observed_name", deposit_type_name_value_4_73, None)
					
					# Retrieve value of data property: deposit_type_source
					deposit_type_source_value_0_74 = resource_data_1["MineralSite"]
					deposit_type_source_index_1_75 = id_deposit_type_candidate_index_1_59
					deposit_type_source_value_1_76 = deposit_type_source_value_0_74[deposit_type_source_index_1_75]
					if not ("deposit_type_candidate" in deposit_type_source_value_1_76):
						pass
					else:
						deposit_type_source_value_2_77 = deposit_type_source_value_1_76["deposit_type_candidate"]
						deposit_type_source_index_3_78 = id_deposit_type_candidate_index_3_64
						deposit_type_source_value_3_79 = deposit_type_source_value_2_77[deposit_type_source_index_3_78]
						if not ("source" in deposit_type_source_value_3_79):
							pass
						else:
							deposit_type_source_value_4_80 = deposit_type_source_value_3_79["source"]
							if not (deposit_type_source_value_4_80 in deposit_type_source_missing_values_6):
								writer_55.write_data_property("https://minmod.isi.edu/resource/source", deposit_type_source_value_4_80, None)
					
					# Retrieve value of data property: deposit_type_normalized_uri
					deposit_type_normalized_uri_value_0_81 = resource_data_1["MineralSite"]
					deposit_type_normalized_uri_index_1_82 = id_deposit_type_candidate_index_1_59
					deposit_type_normalized_uri_value_1_83 = deposit_type_normalized_uri_value_0_81[deposit_type_normalized_uri_index_1_82]
					if not ("deposit_type_candidate" in deposit_type_normalized_uri_value_1_83):
						pass
					else:
						deposit_type_normalized_uri_value_2_84 = deposit_type_normalized_uri_value_1_83["deposit_type_candidate"]
						deposit_type_normalized_uri_index_3_85 = id_deposit_type_candidate_index_3_64
						deposit_type_normalized_uri_value_3_86 = deposit_type_normalized_uri_value_2_84[deposit_type_normalized_uri_index_3_85]
						if not ("normalized_uri" in deposit_type_normalized_uri_value_3_86):
							pass
						else:
							deposit_type_normalized_uri_value_4_87 = deposit_type_normalized_uri_value_3_86["normalized_uri"]
							if not (deposit_type_normalized_uri_value_4_87 in deposit_type_normalized_uri_missing_values_8):
								writer_55.write_data_property("https://minmod.isi.edu/resource/normalized_uri", deposit_type_normalized_uri_value_4_87, "https://purl.org/drepr/1.0/uri")
					
					# Retrieve value of data property: deposit_type_confidence
					deposit_type_confidence_value_0_88 = resource_data_1["MineralSite"]
					deposit_type_confidence_index_1_89 = id_deposit_type_candidate_index_1_59
					deposit_type_confidence_value_1_90 = deposit_type_confidence_value_0_88[deposit_type_confidence_index_1_89]
					if not ("deposit_type_candidate" in deposit_type_confidence_value_1_90):
						pass
					else:
						deposit_type_confidence_value_2_91 = deposit_type_confidence_value_1_90["deposit_type_candidate"]
						deposit_type_confidence_index_3_92 = id_deposit_type_candidate_index_3_64
						deposit_type_confidence_value_3_93 = deposit_type_confidence_value_2_91[deposit_type_confidence_index_3_92]
						if not ("confidence" in deposit_type_confidence_value_3_93):
							pass
						else:
							deposit_type_confidence_value_4_94 = deposit_type_confidence_value_3_93["confidence"]
							if not (deposit_type_confidence_value_4_94 in deposit_type_confidence_missing_values_7):
								writer_55.write_data_property("https://minmod.isi.edu/resource/confidence", deposit_type_confidence_value_4_94, None)
					
					writer_55.end_record()
	
	# Transform records of class mndr:LocationInfo:1
	location_info_country_value_0_95 = resource_data_1["MineralSite"]
	start_96 = 0
	end_97 = len(location_info_country_value_0_95)
	for location_info_country_index_1_98 in range(start_96, end_97):
		location_info_country_value_1_99 = location_info_country_value_0_95[location_info_country_index_1_98]
		if not ("location_info" in location_info_country_value_1_99):
			continue
		else:
			location_info_country_value_2_100 = location_info_country_value_1_99["location_info"]
			if not ("country" in location_info_country_value_2_100):
				continue
			else:
				location_info_country_value_3_101 = location_info_country_value_2_100["country"]
				writer_55.begin_record("https://minmod.isi.edu/resource/LocationInfo", (14, location_info_country_index_1_98), True, False)
				
				# Retrieve value of data property: location_info_country
				if not (location_info_country_value_3_101 in location_info_country_missing_values_11):
					writer_55.write_data_property("https://minmod.isi.edu/resource/country", location_info_country_value_3_101, None)
				
				# Retrieve value of data property: location_info_location_source_record_id
				location_info_location_source_record_id_value_0_102 = resource_data_1["MineralSite"]
				location_info_location_source_record_id_index_1_103 = location_info_country_index_1_98
				location_info_location_source_record_id_value_1_104 = location_info_location_source_record_id_value_0_102[location_info_location_source_record_id_index_1_103]
				if not ("location_info" in location_info_location_source_record_id_value_1_104):
					pass
				else:
					location_info_location_source_record_id_value_2_105 = location_info_location_source_record_id_value_1_104["location_info"]
					if not ("location_source_record_id" in location_info_location_source_record_id_value_2_105):
						pass
					else:
						location_info_location_source_record_id_value_3_106 = location_info_location_source_record_id_value_2_105["location_source_record_id"]
						if not (location_info_location_source_record_id_value_3_106 in location_info_location_source_record_id_missing_values_13):
							writer_55.write_data_property("https://minmod.isi.edu/resource/location_source_record_id", location_info_location_source_record_id_value_3_106, None)
				
				# Retrieve value of data property: location_info_location_source
				location_info_location_source_value_0_107 = resource_data_1["MineralSite"]
				location_info_location_source_index_1_108 = location_info_country_index_1_98
				location_info_location_source_value_1_109 = location_info_location_source_value_0_107[location_info_location_source_index_1_108]
				if not ("location_info" in location_info_location_source_value_1_109):
					pass
				else:
					location_info_location_source_value_2_110 = location_info_location_source_value_1_109["location_info"]
					if not ("location_source" in location_info_location_source_value_2_110):
						pass
					else:
						location_info_location_source_value_3_111 = location_info_location_source_value_2_110["location_source"]
						if not (location_info_location_source_value_3_111 in location_info_location_source_missing_values_14):
							writer_55.write_data_property("https://minmod.isi.edu/resource/location_source", location_info_location_source_value_3_111, None)
				
				# Retrieve value of data property: location_info_crs
				location_info_crs_value_0_112 = resource_data_1["MineralSite"]
				location_info_crs_index_1_113 = location_info_country_index_1_98
				location_info_crs_value_1_114 = location_info_crs_value_0_112[location_info_crs_index_1_113]
				if not ("location_info" in location_info_crs_value_1_114):
					pass
				else:
					location_info_crs_value_2_115 = location_info_crs_value_1_114["location_info"]
					if not ("crs" in location_info_crs_value_2_115):
						pass
					else:
						location_info_crs_value_3_116 = location_info_crs_value_2_115["crs"]
						if not (location_info_crs_value_3_116 in location_info_crs_missing_values_15):
							writer_55.write_data_property("https://minmod.isi.edu/resource/crs", location_info_crs_value_3_116, None)
				
				# Retrieve value of data property: location_info_state
				location_info_state_value_0_117 = resource_data_1["MineralSite"]
				location_info_state_index_1_118 = location_info_country_index_1_98
				location_info_state_value_1_119 = location_info_state_value_0_117[location_info_state_index_1_118]
				if not ("location_info" in location_info_state_value_1_119):
					pass
				else:
					location_info_state_value_2_120 = location_info_state_value_1_119["location_info"]
					if not ("state_or_province" in location_info_state_value_2_120):
						pass
					else:
						location_info_state_value_3_121 = location_info_state_value_2_120["state_or_province"]
						if not (location_info_state_value_3_121 in location_info_state_missing_values_12):
							writer_55.write_data_property("https://minmod.isi.edu/resource/state_or_province", location_info_state_value_3_121, None)
				
				# Retrieve value of data property: location_info_location
				location_info_location_value_0_122 = resource_data_1["MineralSite"]
				location_info_location_index_1_123 = location_info_country_index_1_98
				location_info_location_value_1_124 = location_info_location_value_0_122[location_info_location_index_1_123]
				if not ("location_info" in location_info_location_value_1_124):
					pass
				else:
					location_info_location_value_2_125 = location_info_location_value_1_124["location_info"]
					if not ("location" in location_info_location_value_2_125):
						pass
					else:
						location_info_location_value_3_126 = location_info_location_value_2_125["location"]
						if not (location_info_location_value_3_126 in location_info_location_missing_values_10):
							writer_55.write_data_property("https://minmod.isi.edu/resource/location", location_info_location_value_3_126, "http://www.opengis.net/ont/geosparql#wktLiteral")
				
				writer_55.end_record()
	
	# Transform records of class mndr:Document:1
	id_document_value_0_127 = resource_data_1["MineralSite"]
	start_128 = 0
	end_129 = len(id_document_value_0_127)
	for id_document_index_1_130 in range(start_128, end_129):
		id_document_value_1_131 = id_document_value_0_127[id_document_index_1_130]
		if not ("mineral_inventory" in id_document_value_1_131):
			continue
		else:
			id_document_value_2_132 = id_document_value_1_131["mineral_inventory"]
			start_133 = 0
			end_134 = len(id_document_value_2_132)
			for id_document_index_3_135 in range(start_133, end_134):
				id_document_value_3_136 = id_document_value_2_132[id_document_index_3_135]
				if not ("reference" in id_document_value_3_136):
					continue
				else:
					id_document_value_4_137 = id_document_value_3_136["reference"]
					if not ("document" in id_document_value_4_137):
						continue
					else:
						id_document_value_5_138 = id_document_value_4_137["document"]
						if not ("id" in id_document_value_5_138):
							continue
						else:
							id_document_value_6_139 = id_document_value_5_138["id"]
							if id_document_value_6_139 in id_document_missing_values_37:
								continue
							writer_55.begin_record("https://minmod.isi.edu/resource/Document", id_document_value_6_139, False, False)
							
							# Retrieve value of data property: uri_document
							uri_document_value_0_140 = resource_data_1["MineralSite"]
							uri_document_index_1_141 = id_document_index_1_130
							uri_document_value_1_142 = uri_document_value_0_140[uri_document_index_1_141]
							if not ("mineral_inventory" in uri_document_value_1_142):
								pass
							else:
								uri_document_value_2_143 = uri_document_value_1_142["mineral_inventory"]
								uri_document_index_3_144 = id_document_index_3_135
								uri_document_value_3_145 = uri_document_value_2_143[uri_document_index_3_144]
								if not ("reference" in uri_document_value_3_145):
									pass
								else:
									uri_document_value_4_146 = uri_document_value_3_145["reference"]
									if not ("document" in uri_document_value_4_146):
										pass
									else:
										uri_document_value_5_147 = uri_document_value_4_146["document"]
										if not ("uri" in uri_document_value_5_147):
											pass
										else:
											uri_document_value_6_148 = uri_document_value_5_147["uri"]
											if not (uri_document_value_6_148 in uri_document_missing_values_39):
												writer_55.write_data_property("https://minmod.isi.edu/resource/uri", uri_document_value_6_148, None)
							
							# Retrieve value of data property: doi
							doi_value_0_149 = resource_data_1["MineralSite"]
							doi_index_1_150 = id_document_index_1_130
							doi_value_1_151 = doi_value_0_149[doi_index_1_150]
							if not ("mineral_inventory" in doi_value_1_151):
								pass
							else:
								doi_value_2_152 = doi_value_1_151["mineral_inventory"]
								doi_index_3_153 = id_document_index_3_135
								doi_value_3_154 = doi_value_2_152[doi_index_3_153]
								if not ("reference" in doi_value_3_154):
									pass
								else:
									doi_value_4_155 = doi_value_3_154["reference"]
									if not ("document" in doi_value_4_155):
										pass
									else:
										doi_value_5_156 = doi_value_4_155["document"]
										if not ("doi" in doi_value_5_156):
											pass
										else:
											doi_value_6_157 = doi_value_5_156["doi"]
											if not (doi_value_6_157 in doi_missing_values_40):
												writer_55.write_data_property("https://minmod.isi.edu/resource/doi", doi_value_6_157, None)
							
							# Retrieve value of data property: journal
							journal_value_0_158 = resource_data_1["MineralSite"]
							journal_index_1_159 = id_document_index_1_130
							journal_value_1_160 = journal_value_0_158[journal_index_1_159]
							if not ("mineral_inventory" in journal_value_1_160):
								pass
							else:
								journal_value_2_161 = journal_value_1_160["mineral_inventory"]
								journal_index_3_162 = id_document_index_3_135
								journal_value_3_163 = journal_value_2_161[journal_index_3_162]
								if not ("reference" in journal_value_3_163):
									pass
								else:
									journal_value_4_164 = journal_value_3_163["reference"]
									if not ("document" in journal_value_4_164):
										pass
									else:
										journal_value_5_165 = journal_value_4_164["document"]
										if not ("journal" in journal_value_5_165):
											pass
										else:
											journal_value_6_166 = journal_value_5_165["journal"]
											if not (journal_value_6_166 in journal_missing_values_44):
												writer_55.write_data_property("https://minmod.isi.edu/resource/journal", journal_value_6_166, None)
							
							# Retrieve value of data property: authors
							authors_value_0_167 = resource_data_1["MineralSite"]
							authors_index_1_168 = id_document_index_1_130
							authors_value_1_169 = authors_value_0_167[authors_index_1_168]
							if not ("mineral_inventory" in authors_value_1_169):
								pass
							else:
								authors_value_2_170 = authors_value_1_169["mineral_inventory"]
								authors_index_3_171 = id_document_index_3_135
								authors_value_3_172 = authors_value_2_170[authors_index_3_171]
								if not ("reference" in authors_value_3_172):
									pass
								else:
									authors_value_4_173 = authors_value_3_172["reference"]
									if not ("document" in authors_value_4_173):
										pass
									else:
										authors_value_5_174 = authors_value_4_173["document"]
										if not ("authors" in authors_value_5_174):
											pass
										else:
											authors_value_6_175 = authors_value_5_174["authors"]
											if True:
												writer_55.write_data_property("https://minmod.isi.edu/resource/authors", authors_value_6_175, None)
							
							# Retrieve value of data property: description_document
							description_document_value_0_176 = resource_data_1["MineralSite"]
							description_document_index_1_177 = id_document_index_1_130
							description_document_value_1_178 = description_document_value_0_176[description_document_index_1_177]
							if not ("mineral_inventory" in description_document_value_1_178):
								pass
							else:
								description_document_value_2_179 = description_document_value_1_178["mineral_inventory"]
								description_document_index_3_180 = id_document_index_3_135
								description_document_value_3_181 = description_document_value_2_179[description_document_index_3_180]
								if not ("reference" in description_document_value_3_181):
									pass
								else:
									description_document_value_4_182 = description_document_value_3_181["reference"]
									if not ("document" in description_document_value_4_182):
										pass
									else:
										description_document_value_5_183 = description_document_value_4_182["document"]
										if not ("description" in description_document_value_5_183):
											pass
										else:
											description_document_value_6_184 = description_document_value_5_183["description"]
											if not (description_document_value_6_184 in description_document_missing_values_45):
												writer_55.write_data_property("https://minmod.isi.edu/resource/description", description_document_value_6_184, None)
							
							# Retrieve value of data property: title_document
							title_document_value_0_185 = resource_data_1["MineralSite"]
							title_document_index_1_186 = id_document_index_1_130
							title_document_value_1_187 = title_document_value_0_185[title_document_index_1_186]
							if not ("mineral_inventory" in title_document_value_1_187):
								pass
							else:
								title_document_value_2_188 = title_document_value_1_187["mineral_inventory"]
								title_document_index_3_189 = id_document_index_3_135
								title_document_value_3_190 = title_document_value_2_188[title_document_index_3_189]
								if not ("reference" in title_document_value_3_190):
									pass
								else:
									title_document_value_4_191 = title_document_value_3_190["reference"]
									if not ("document" in title_document_value_4_191):
										pass
									else:
										title_document_value_5_192 = title_document_value_4_191["document"]
										if not ("title" in title_document_value_5_192):
											pass
										else:
											title_document_value_6_193 = title_document_value_5_192["title"]
											if not (title_document_value_6_193 in title_document_missing_values_46):
												writer_55.write_data_property("https://minmod.isi.edu/resource/title", title_document_value_6_193, None)
							
							# Retrieve value of data property: volume
							volume_value_0_194 = resource_data_1["MineralSite"]
							volume_index_1_195 = id_document_index_1_130
							volume_value_1_196 = volume_value_0_194[volume_index_1_195]
							if not ("mineral_inventory" in volume_value_1_196):
								pass
							else:
								volume_value_2_197 = volume_value_1_196["mineral_inventory"]
								volume_index_3_198 = id_document_index_3_135
								volume_value_3_199 = volume_value_2_197[volume_index_3_198]
								if not ("reference" in volume_value_3_199):
									pass
								else:
									volume_value_4_200 = volume_value_3_199["reference"]
									if not ("document" in volume_value_4_200):
										pass
									else:
										volume_value_5_201 = volume_value_4_200["document"]
										if not ("volume" in volume_value_5_201):
											pass
										else:
											volume_value_6_202 = volume_value_5_201["volume"]
											if not (volume_value_6_202 in volume_missing_values_41):
												writer_55.write_data_property("https://minmod.isi.edu/resource/volume", volume_value_6_202, None)
							
							# Retrieve value of data property: issue_document
							issue_document_value_0_203 = resource_data_1["MineralSite"]
							issue_document_index_1_204 = id_document_index_1_130
							issue_document_value_1_205 = issue_document_value_0_203[issue_document_index_1_204]
							if not ("mineral_inventory" in issue_document_value_1_205):
								pass
							else:
								issue_document_value_2_206 = issue_document_value_1_205["mineral_inventory"]
								issue_document_index_3_207 = id_document_index_3_135
								issue_document_value_3_208 = issue_document_value_2_206[issue_document_index_3_207]
								if not ("reference" in issue_document_value_3_208):
									pass
								else:
									issue_document_value_4_209 = issue_document_value_3_208["reference"]
									if not ("document" in issue_document_value_4_209):
										pass
									else:
										issue_document_value_5_210 = issue_document_value_4_209["document"]
										if not ("issue" in issue_document_value_5_210):
											pass
										else:
											issue_document_value_6_211 = issue_document_value_5_210["issue"]
											if not (issue_document_value_6_211 in issue_document_missing_values_36):
												writer_55.write_data_property("https://minmod.isi.edu/resource/issue", issue_document_value_6_211, None)
							
							# Retrieve value of data property: month_document
							month_document_value_0_212 = resource_data_1["MineralSite"]
							month_document_index_1_213 = id_document_index_1_130
							month_document_value_1_214 = month_document_value_0_212[month_document_index_1_213]
							if not ("mineral_inventory" in month_document_value_1_214):
								pass
							else:
								month_document_value_2_215 = month_document_value_1_214["mineral_inventory"]
								month_document_index_3_216 = id_document_index_3_135
								month_document_value_3_217 = month_document_value_2_215[month_document_index_3_216]
								if not ("reference" in month_document_value_3_217):
									pass
								else:
									month_document_value_4_218 = month_document_value_3_217["reference"]
									if not ("document" in month_document_value_4_218):
										pass
									else:
										month_document_value_5_219 = month_document_value_4_218["document"]
										if not ("month" in month_document_value_5_219):
											pass
										else:
											month_document_value_6_220 = month_document_value_5_219["month"]
											if not (month_document_value_6_220 in month_document_missing_values_43):
												writer_55.write_data_property("https://minmod.isi.edu/resource/month", month_document_value_6_220, None)
							
							# Retrieve value of data property: year_document
							year_document_value_0_221 = resource_data_1["MineralSite"]
							year_document_index_1_222 = id_document_index_1_130
							year_document_value_1_223 = year_document_value_0_221[year_document_index_1_222]
							if not ("mineral_inventory" in year_document_value_1_223):
								pass
							else:
								year_document_value_2_224 = year_document_value_1_223["mineral_inventory"]
								year_document_index_3_225 = id_document_index_3_135
								year_document_value_3_226 = year_document_value_2_224[year_document_index_3_225]
								if not ("reference" in year_document_value_3_226):
									pass
								else:
									year_document_value_4_227 = year_document_value_3_226["reference"]
									if not ("document" in year_document_value_4_227):
										pass
									else:
										year_document_value_5_228 = year_document_value_4_227["document"]
										if not ("year" in year_document_value_5_228):
											pass
										else:
											year_document_value_6_229 = year_document_value_5_228["year"]
											if not (year_document_value_6_229 in year_document_missing_values_42):
												writer_55.write_data_property("https://minmod.isi.edu/resource/year", year_document_value_6_229, None)
							
							writer_55.end_record()
	
	# Transform records of class mndr:BoundingBox:1
	x_min_value_0_230 = resource_data_1["MineralSite"]
	start_231 = 0
	end_232 = len(x_min_value_0_230)
	for x_min_index_1_233 in range(start_231, end_232):
		x_min_value_1_234 = x_min_value_0_230[x_min_index_1_233]
		if not ("mineral_inventory" in x_min_value_1_234):
			continue
		else:
			x_min_value_2_235 = x_min_value_1_234["mineral_inventory"]
			start_236 = 0
			end_237 = len(x_min_value_2_235)
			for x_min_index_3_238 in range(start_236, end_237):
				x_min_value_3_239 = x_min_value_2_235[x_min_index_3_238]
				if not ("reference" in x_min_value_3_239):
					continue
				else:
					x_min_value_4_240 = x_min_value_3_239["reference"]
					if not ("page_info" in x_min_value_4_240):
						continue
					else:
						x_min_value_5_241 = x_min_value_4_240["page_info"]
						start_242 = 0
						end_243 = len(x_min_value_5_241)
						for x_min_index_6_244 in range(start_242, end_243):
							x_min_value_6_245 = x_min_value_5_241[x_min_index_6_244]
							if not ("bounding_box" in x_min_value_6_245):
								continue
							else:
								x_min_value_7_246 = x_min_value_6_245["bounding_box"]
								if not ("x_min" in x_min_value_7_246):
									continue
								else:
									x_min_value_8_247 = x_min_value_7_246["x_min"]
									writer_55.begin_record("https://minmod.isi.edu/resource/BoundingBox", (55, x_min_index_1_233, x_min_index_3_238, x_min_index_6_244), True, False)
									
									# Retrieve value of data property: x_min
									if not (x_min_value_8_247 in x_min_missing_values_50):
										writer_55.write_data_property("https://minmod.isi.edu/resource/x_min", x_min_value_8_247, None)
									
									# Retrieve value of data property: x_max
									x_max_value_0_248 = resource_data_1["MineralSite"]
									x_max_index_1_249 = x_min_index_1_233
									x_max_value_1_250 = x_max_value_0_248[x_max_index_1_249]
									if not ("mineral_inventory" in x_max_value_1_250):
										pass
									else:
										x_max_value_2_251 = x_max_value_1_250["mineral_inventory"]
										x_max_index_3_252 = x_min_index_3_238
										x_max_value_3_253 = x_max_value_2_251[x_max_index_3_252]
										if not ("reference" in x_max_value_3_253):
											pass
										else:
											x_max_value_4_254 = x_max_value_3_253["reference"]
											if not ("page_info" in x_max_value_4_254):
												pass
											else:
												x_max_value_5_255 = x_max_value_4_254["page_info"]
												x_max_index_6_256 = x_min_index_6_244
												x_max_value_6_257 = x_max_value_5_255[x_max_index_6_256]
												if not ("bounding_box" in x_max_value_6_257):
													pass
												else:
													x_max_value_7_258 = x_max_value_6_257["bounding_box"]
													if not ("x_max" in x_max_value_7_258):
														pass
													else:
														x_max_value_8_259 = x_max_value_7_258["x_max"]
														if not (x_max_value_8_259 in x_max_missing_values_51):
															writer_55.write_data_property("https://minmod.isi.edu/resource/x_max", x_max_value_8_259, None)
									
									# Retrieve value of data property: y_min
									y_min_value_0_260 = resource_data_1["MineralSite"]
									y_min_index_1_261 = x_min_index_1_233
									y_min_value_1_262 = y_min_value_0_260[y_min_index_1_261]
									if not ("mineral_inventory" in y_min_value_1_262):
										pass
									else:
										y_min_value_2_263 = y_min_value_1_262["mineral_inventory"]
										y_min_index_3_264 = x_min_index_3_238
										y_min_value_3_265 = y_min_value_2_263[y_min_index_3_264]
										if not ("reference" in y_min_value_3_265):
											pass
										else:
											y_min_value_4_266 = y_min_value_3_265["reference"]
											if not ("page_info" in y_min_value_4_266):
												pass
											else:
												y_min_value_5_267 = y_min_value_4_266["page_info"]
												y_min_index_6_268 = x_min_index_6_244
												y_min_value_6_269 = y_min_value_5_267[y_min_index_6_268]
												if not ("bounding_box" in y_min_value_6_269):
													pass
												else:
													y_min_value_7_270 = y_min_value_6_269["bounding_box"]
													if not ("y_min" in y_min_value_7_270):
														pass
													else:
														y_min_value_8_271 = y_min_value_7_270["y_min"]
														if not (y_min_value_8_271 in y_min_missing_values_52):
															writer_55.write_data_property("https://minmod.isi.edu/resource/y_min", y_min_value_8_271, None)
									
									# Retrieve value of data property: y_max
									y_max_value_0_272 = resource_data_1["MineralSite"]
									y_max_index_1_273 = x_min_index_1_233
									y_max_value_1_274 = y_max_value_0_272[y_max_index_1_273]
									if not ("mineral_inventory" in y_max_value_1_274):
										pass
									else:
										y_max_value_2_275 = y_max_value_1_274["mineral_inventory"]
										y_max_index_3_276 = x_min_index_3_238
										y_max_value_3_277 = y_max_value_2_275[y_max_index_3_276]
										if not ("reference" in y_max_value_3_277):
											pass
										else:
											y_max_value_4_278 = y_max_value_3_277["reference"]
											if not ("page_info" in y_max_value_4_278):
												pass
											else:
												y_max_value_5_279 = y_max_value_4_278["page_info"]
												y_max_index_6_280 = x_min_index_6_244
												y_max_value_6_281 = y_max_value_5_279[y_max_index_6_280]
												if not ("bounding_box" in y_max_value_6_281):
													pass
												else:
													y_max_value_7_282 = y_max_value_6_281["bounding_box"]
													if not ("y_max" in y_max_value_7_282):
														pass
													else:
														y_max_value_8_283 = y_max_value_7_282["y_max"]
														if not (y_max_value_8_283 in y_max_missing_values_53):
															writer_55.write_data_property("https://minmod.isi.edu/resource/y_max", y_max_value_8_283, None)
									
									writer_55.end_record()
	
	# Transform records of class mndr:PageInfo:1
	page_value_0_284 = resource_data_1["MineralSite"]
	start_285 = 0
	end_286 = len(page_value_0_284)
	for page_index_1_287 in range(start_285, end_286):
		page_value_1_288 = page_value_0_284[page_index_1_287]
		if not ("mineral_inventory" in page_value_1_288):
			continue
		else:
			page_value_2_289 = page_value_1_288["mineral_inventory"]
			start_290 = 0
			end_291 = len(page_value_2_289)
			for page_index_3_292 in range(start_290, end_291):
				page_value_3_293 = page_value_2_289[page_index_3_292]
				if not ("reference" in page_value_3_293):
					continue
				else:
					page_value_4_294 = page_value_3_293["reference"]
					if not ("page_info" in page_value_4_294):
						continue
					else:
						page_value_5_295 = page_value_4_294["page_info"]
						start_296 = 0
						end_297 = len(page_value_5_295)
						for page_index_6_298 in range(start_296, end_297):
							page_value_6_299 = page_value_5_295[page_index_6_298]
							if not ("page" in page_value_6_299):
								continue
							else:
								page_value_7_300 = page_value_6_299["page"]
								writer_55.begin_record("https://minmod.isi.edu/resource/PageInfo", (59, page_index_1_287, page_index_3_292, page_index_6_298), True, False)
								
								# Retrieve value of data property: page
								if not (page_value_7_300 in page_missing_values_54):
									writer_55.write_data_property("https://minmod.isi.edu/resource/page", page_value_7_300, None)
								
								# Retrieve value of object property: x_min
								x_min_value_0_301 = resource_data_1["MineralSite"]
								x_min_index_1_302 = page_index_1_287
								x_min_value_1_303 = x_min_value_0_301[x_min_index_1_302]
								if not ("mineral_inventory" in x_min_value_1_303):
									pass
								else:
									x_min_value_2_304 = x_min_value_1_303["mineral_inventory"]
									x_min_index_3_305 = page_index_3_292
									x_min_value_3_306 = x_min_value_2_304[x_min_index_3_305]
									if not ("reference" in x_min_value_3_306):
										pass
									else:
										x_min_value_4_307 = x_min_value_3_306["reference"]
										if not ("page_info" in x_min_value_4_307):
											pass
										else:
											x_min_value_5_308 = x_min_value_4_307["page_info"]
											x_min_index_6_309 = page_index_6_298
											x_min_value_6_310 = x_min_value_5_308[x_min_index_6_309]
											if not ("bounding_box" in x_min_value_6_310):
												pass
											else:
												x_min_value_7_311 = x_min_value_6_310["bounding_box"]
												if not ("x_min" in x_min_value_7_311):
													pass
												else:
													x_min_value_8_312 = x_min_value_7_311["x_min"]
													if writer_55.has_written_record((55, x_min_index_1_302, x_min_index_3_305, x_min_index_6_309)):
														writer_55.write_object_property("https://minmod.isi.edu/resource/bounding_box", (55, x_min_index_1_302, x_min_index_3_305, x_min_index_6_309), True, True, False)
								
								writer_55.end_record()
	
	# Transform records of class mndr:Reference:1
	id_document_ref_value_0_313 = resource_data_1["MineralSite"]
	start_314 = 0
	end_315 = len(id_document_ref_value_0_313)
	for id_document_ref_index_1_316 in range(start_314, end_315):
		id_document_ref_value_1_317 = id_document_ref_value_0_313[id_document_ref_index_1_316]
		if not ("mineral_inventory" in id_document_ref_value_1_317):
			continue
		else:
			id_document_ref_value_2_318 = id_document_ref_value_1_317["mineral_inventory"]
			start_319 = 0
			end_320 = len(id_document_ref_value_2_318)
			for id_document_ref_index_3_321 in range(start_319, end_320):
				id_document_ref_value_3_322 = id_document_ref_value_2_318[id_document_ref_index_3_321]
				if not ("reference" in id_document_ref_value_3_322):
					continue
				else:
					id_document_ref_value_4_323 = id_document_ref_value_3_322["reference"]
					if not ("document" in id_document_ref_value_4_323):
						continue
					else:
						id_document_ref_value_5_324 = id_document_ref_value_4_323["document"]
						if not ("id" in id_document_ref_value_5_324):
							continue
						else:
							id_document_ref_value_6_325 = id_document_ref_value_5_324["id"]
							if ((42, id_document_ref_value_6_325)) in id_document_ref_missing_values_38:
								continue
							writer_55.begin_record("https://minmod.isi.edu/resource/Reference", (42, id_document_ref_value_6_325), True, False)
							
							# Retrieve value of object property: id_document
							id_document_value_0_326 = resource_data_1["MineralSite"]
							id_document_index_1_327 = id_document_ref_index_1_316
							id_document_value_1_328 = id_document_value_0_326[id_document_index_1_327]
							if not ("mineral_inventory" in id_document_value_1_328):
								pass
							else:
								id_document_value_2_329 = id_document_value_1_328["mineral_inventory"]
								id_document_index_3_330 = id_document_ref_index_3_321
								id_document_value_3_331 = id_document_value_2_329[id_document_index_3_330]
								if not ("reference" in id_document_value_3_331):
									pass
								else:
									id_document_value_4_332 = id_document_value_3_331["reference"]
									if not ("document" in id_document_value_4_332):
										pass
									else:
										id_document_value_5_333 = id_document_value_4_332["document"]
										if not ("id" in id_document_value_5_333):
											pass
										else:
											id_document_value_6_334 = id_document_value_5_333["id"]
											if writer_55.has_written_record(id_document_value_6_334):
												writer_55.write_object_property("https://minmod.isi.edu/resource/document", id_document_value_6_334, True, False, False)
							
							# Retrieve value of object property: page
							page_value_0_335 = resource_data_1["MineralSite"]
							page_index_1_336 = id_document_ref_index_1_316
							page_value_1_337 = page_value_0_335[page_index_1_336]
							if not ("mineral_inventory" in page_value_1_337):
								pass
							else:
								page_value_2_338 = page_value_1_337["mineral_inventory"]
								page_index_3_339 = id_document_ref_index_3_321
								page_value_3_340 = page_value_2_338[page_index_3_339]
								if not ("reference" in page_value_3_340):
									pass
								else:
									page_value_4_341 = page_value_3_340["reference"]
									if not ("page_info" in page_value_4_341):
										pass
									else:
										page_value_5_342 = page_value_4_341["page_info"]
										start_343 = 0
										end_344 = len(page_value_5_342)
										for page_index_6_345 in range(start_343, end_344):
											page_value_6_346 = page_value_5_342[page_index_6_345]
											if not ("page" in page_value_6_346):
												pass
											else:
												page_value_7_347 = page_value_6_346["page"]
												if writer_55.has_written_record((59, page_index_1_336, page_index_3_339, page_index_6_345)):
													writer_55.write_object_property("https://minmod.isi.edu/resource/page_info", (59, page_index_1_336, page_index_3_339, page_index_6_345), True, True, False)
							
							writer_55.end_record()
	
	# Transform records of class mndr:Ore:1
	ore_unit_value_0_348 = resource_data_1["MineralSite"]
	start_349 = 0
	end_350 = len(ore_unit_value_0_348)
	for ore_unit_index_1_351 in range(start_349, end_350):
		ore_unit_value_1_352 = ore_unit_value_0_348[ore_unit_index_1_351]
		if not ("mineral_inventory" in ore_unit_value_1_352):
			continue
		else:
			ore_unit_value_2_353 = ore_unit_value_1_352["mineral_inventory"]
			start_354 = 0
			end_355 = len(ore_unit_value_2_353)
			for ore_unit_index_3_356 in range(start_354, end_355):
				ore_unit_value_3_357 = ore_unit_value_2_353[ore_unit_index_3_356]
				if not ("ore" in ore_unit_value_3_357):
					continue
				else:
					ore_unit_value_4_358 = ore_unit_value_3_357["ore"]
					if not ("ore_unit" in ore_unit_value_4_358):
						continue
					else:
						ore_unit_value_5_359 = ore_unit_value_4_358["ore_unit"]
						writer_55.begin_record("https://minmod.isi.edu/resource/Ore", (33, ore_unit_index_1_351, ore_unit_index_3_356), True, False)
						
						# Retrieve value of data property: ore_value
						ore_value_value_0_360 = resource_data_1["MineralSite"]
						ore_value_index_1_361 = ore_unit_index_1_351
						ore_value_value_1_362 = ore_value_value_0_360[ore_value_index_1_361]
						if not ("mineral_inventory" in ore_value_value_1_362):
							pass
						else:
							ore_value_value_2_363 = ore_value_value_1_362["mineral_inventory"]
							ore_value_index_3_364 = ore_unit_index_3_356
							ore_value_value_3_365 = ore_value_value_2_363[ore_value_index_3_364]
							if not ("ore" in ore_value_value_3_365):
								pass
							else:
								ore_value_value_4_366 = ore_value_value_3_365["ore"]
								if not ("ore_value" in ore_value_value_4_366):
									pass
								else:
									ore_value_value_5_367 = ore_value_value_4_366["ore_value"]
									if not (ore_value_value_5_367 in ore_value_missing_values_26):
										writer_55.write_data_property("https://minmod.isi.edu/resource/ore_value", ore_value_value_5_367, "http://www.w3.org/2001/XMLSchema#decimal")
						
						# Retrieve value of data property: ore_unit
						if not (ore_unit_value_5_359 in ore_unit_missing_values_30):
							writer_55.write_data_property("https://minmod.isi.edu/resource/ore_unit", ore_unit_value_5_359, "https://purl.org/drepr/1.0/uri")
						
						writer_55.end_record()
	
	# Transform records of class mndr:Grade:1
	grade_unit_value_0_368 = resource_data_1["MineralSite"]
	start_369 = 0
	end_370 = len(grade_unit_value_0_368)
	for grade_unit_index_1_371 in range(start_369, end_370):
		grade_unit_value_1_372 = grade_unit_value_0_368[grade_unit_index_1_371]
		if not ("mineral_inventory" in grade_unit_value_1_372):
			continue
		else:
			grade_unit_value_2_373 = grade_unit_value_1_372["mineral_inventory"]
			start_374 = 0
			end_375 = len(grade_unit_value_2_373)
			for grade_unit_index_3_376 in range(start_374, end_375):
				grade_unit_value_3_377 = grade_unit_value_2_373[grade_unit_index_3_376]
				if not ("grade" in grade_unit_value_3_377):
					continue
				else:
					grade_unit_value_4_378 = grade_unit_value_3_377["grade"]
					if not ("grade_unit" in grade_unit_value_4_378):
						continue
					else:
						grade_unit_value_5_379 = grade_unit_value_4_378["grade_unit"]
						writer_55.begin_record("https://minmod.isi.edu/resource/Grade", (34, grade_unit_index_1_371, grade_unit_index_3_376), True, False)
						
						# Retrieve value of data property: grade_value
						grade_value_value_0_380 = resource_data_1["MineralSite"]
						grade_value_index_1_381 = grade_unit_index_1_371
						grade_value_value_1_382 = grade_value_value_0_380[grade_value_index_1_381]
						if not ("mineral_inventory" in grade_value_value_1_382):
							pass
						else:
							grade_value_value_2_383 = grade_value_value_1_382["mineral_inventory"]
							grade_value_index_3_384 = grade_unit_index_3_376
							grade_value_value_3_385 = grade_value_value_2_383[grade_value_index_3_384]
							if not ("grade" in grade_value_value_3_385):
								pass
							else:
								grade_value_value_4_386 = grade_value_value_3_385["grade"]
								if not ("grade_value" in grade_value_value_4_386):
									pass
								else:
									grade_value_value_5_387 = grade_value_value_4_386["grade_value"]
									if not (grade_value_value_5_387 in grade_value_missing_values_27):
										writer_55.write_data_property("https://minmod.isi.edu/resource/grade_value", grade_value_value_5_387, "http://www.w3.org/2001/XMLSchema#decimal")
						
						# Retrieve value of data property: grade_unit
						if not (grade_unit_value_5_379 in grade_unit_missing_values_31):
							writer_55.write_data_property("https://minmod.isi.edu/resource/grade_unit", grade_unit_value_5_379, "https://purl.org/drepr/1.0/uri")
						
						writer_55.end_record()
	
	# Transform records of class mndr:Grade:2
	cutoff_grade_unit_value_0_388 = resource_data_1["MineralSite"]
	start_389 = 0
	end_390 = len(cutoff_grade_unit_value_0_388)
	for cutoff_grade_unit_index_1_391 in range(start_389, end_390):
		cutoff_grade_unit_value_1_392 = cutoff_grade_unit_value_0_388[cutoff_grade_unit_index_1_391]
		if not ("mineral_inventory" in cutoff_grade_unit_value_1_392):
			continue
		else:
			cutoff_grade_unit_value_2_393 = cutoff_grade_unit_value_1_392["mineral_inventory"]
			start_394 = 0
			end_395 = len(cutoff_grade_unit_value_2_393)
			for cutoff_grade_unit_index_3_396 in range(start_394, end_395):
				cutoff_grade_unit_value_3_397 = cutoff_grade_unit_value_2_393[cutoff_grade_unit_index_3_396]
				if not ("cutoff_grade" in cutoff_grade_unit_value_3_397):
					continue
				else:
					cutoff_grade_unit_value_4_398 = cutoff_grade_unit_value_3_397["cutoff_grade"]
					if not ("grade_unit" in cutoff_grade_unit_value_4_398):
						continue
					else:
						cutoff_grade_unit_value_5_399 = cutoff_grade_unit_value_4_398["grade_unit"]
						writer_55.begin_record("https://minmod.isi.edu/resource/Grade", (32, cutoff_grade_unit_index_1_391, cutoff_grade_unit_index_3_396), True, False)
						
						# Retrieve value of data property: cutoff_grade_value
						cutoff_grade_value_value_0_400 = resource_data_1["MineralSite"]
						cutoff_grade_value_index_1_401 = cutoff_grade_unit_index_1_391
						cutoff_grade_value_value_1_402 = cutoff_grade_value_value_0_400[cutoff_grade_value_index_1_401]
						if not ("mineral_inventory" in cutoff_grade_value_value_1_402):
							pass
						else:
							cutoff_grade_value_value_2_403 = cutoff_grade_value_value_1_402["mineral_inventory"]
							cutoff_grade_value_index_3_404 = cutoff_grade_unit_index_3_396
							cutoff_grade_value_value_3_405 = cutoff_grade_value_value_2_403[cutoff_grade_value_index_3_404]
							if not ("cutoff_grade" in cutoff_grade_value_value_3_405):
								pass
							else:
								cutoff_grade_value_value_4_406 = cutoff_grade_value_value_3_405["cutoff_grade"]
								if not ("grade_value" in cutoff_grade_value_value_4_406):
									pass
								else:
									cutoff_grade_value_value_5_407 = cutoff_grade_value_value_4_406["grade_value"]
									if not (cutoff_grade_value_value_5_407 in cutoff_grade_value_missing_values_28):
										writer_55.write_data_property("https://minmod.isi.edu/resource/grade_value", cutoff_grade_value_value_5_407, "http://www.w3.org/2001/XMLSchema#decimal")
						
						# Retrieve value of data property: cutoff_grade_unit
						if not (cutoff_grade_unit_value_5_399 in cutoff_grade_unit_missing_values_29):
							writer_55.write_data_property("https://minmod.isi.edu/resource/grade_unit", cutoff_grade_unit_value_5_399, "https://purl.org/drepr/1.0/uri")
						
						writer_55.end_record()
	
	# Transform records of class mndr:Category:1
	category_value_0_408 = resource_data_1["MineralSite"]
	start_409 = 0
	end_410 = len(category_value_0_408)
	for category_index_1_411 in range(start_409, end_410):
		category_value_1_412 = category_value_0_408[category_index_1_411]
		if not ("mineral_inventory" in category_value_1_412):
			continue
		else:
			category_value_2_413 = category_value_1_412["mineral_inventory"]
			start_414 = 0
			end_415 = len(category_value_2_413)
			for category_index_3_416 in range(start_414, end_415):
				category_value_3_417 = category_value_2_413[category_index_3_416]
				if not ("category" in category_value_3_417):
					continue
				else:
					category_value_4_418 = category_value_3_417["category"]
					start_419 = 0
					end_420 = len(category_value_4_418)
					for category_index_5_421 in range(start_419, end_420):
						category_value_5_422 = category_value_4_418[category_index_5_421]
						if category_value_5_422 in category_missing_values_32:
							continue
						writer_55.begin_record("https://minmod.isi.edu/resource/Category", category_value_5_422, False, False)
						
						writer_55.end_record()
	
	# Transform records of class mndr:MineralInventory:1
	id_value_0_423 = resource_data_1["MineralSite"]
	start_424 = 0
	end_425 = len(id_value_0_423)
	for id_index_1_426 in range(start_424, end_425):
		id_value_1_427 = id_value_0_423[id_index_1_426]
		if not ("mineral_inventory" in id_value_1_427):
			continue
		else:
			id_value_2_428 = id_value_1_427["mineral_inventory"]
			start_429 = 0
			end_430 = len(id_value_2_428)
			for id_index_3_431 in range(start_429, end_430):
				id_value_3_432 = id_value_2_428[id_index_3_431]
				id_value_4_433 = id_value_3_432["id"]
				writer_55.begin_record("https://minmod.isi.edu/resource/MineralInventory", id_value_4_433, False, False)
				
				# Retrieve value of data property: id
				if True:
					writer_55.write_data_property("https://minmod.isi.edu/resource/id", id_value_4_433, None)
				
				# Retrieve value of data property: date
				date_value_0_434 = resource_data_1["MineralSite"]
				date_index_1_435 = id_index_1_426
				date_value_1_436 = date_value_0_434[date_index_1_435]
				if not ("mineral_inventory" in date_value_1_436):
					pass
				else:
					date_value_2_437 = date_value_1_436["mineral_inventory"]
					date_index_3_438 = id_index_3_431
					date_value_3_439 = date_value_2_437[date_index_3_438]
					if not ("date" in date_value_3_439):
						pass
					else:
						date_value_4_440 = date_value_3_439["date"]
						if not (date_value_4_440 in date_missing_values_33):
							writer_55.write_data_property("https://minmod.isi.edu/resource/date", date_value_4_440, "http://www.w3.org/2001/XMLSchema#date")
				
				# Retrieve value of data property: zone
				zone_value_0_441 = resource_data_1["MineralSite"]
				zone_index_1_442 = id_index_1_426
				zone_value_1_443 = zone_value_0_441[zone_index_1_442]
				if not ("mineral_inventory" in zone_value_1_443):
					pass
				else:
					zone_value_2_444 = zone_value_1_443["mineral_inventory"]
					zone_index_3_445 = id_index_3_431
					zone_value_3_446 = zone_value_2_444[zone_index_3_445]
					if not ("zone" in zone_value_3_446):
						pass
					else:
						zone_value_4_447 = zone_value_3_446["zone"]
						if not (zone_value_4_447 in zone_missing_values_34):
							writer_55.write_data_property("https://minmod.isi.edu/resource/zone", zone_value_4_447, None)
				
				# Retrieve value of data property: commodity
				commodity_value_0_448 = resource_data_1["MineralSite"]
				commodity_index_1_449 = id_index_1_426
				commodity_value_1_450 = commodity_value_0_448[commodity_index_1_449]
				if not ("mineral_inventory" in commodity_value_1_450):
					pass
				else:
					commodity_value_2_451 = commodity_value_1_450["mineral_inventory"]
					commodity_index_3_452 = id_index_3_431
					commodity_value_3_453 = commodity_value_2_451[commodity_index_3_452]
					if not ("commodity" in commodity_value_3_453):
						pass
					else:
						commodity_value_4_454 = commodity_value_3_453["commodity"]
						if not (commodity_value_4_454 in commodity_missing_values_23):
							writer_55.write_data_property("https://minmod.isi.edu/resource/commodity", commodity_value_4_454, "https://purl.org/drepr/1.0/uri")
				
				# Retrieve value of data property: observed_commodity
				observed_commodity_value_0_455 = resource_data_1["MineralSite"]
				observed_commodity_index_1_456 = id_index_1_426
				observed_commodity_value_1_457 = observed_commodity_value_0_455[observed_commodity_index_1_456]
				if not ("mineral_inventory" in observed_commodity_value_1_457):
					pass
				else:
					observed_commodity_value_2_458 = observed_commodity_value_1_457["mineral_inventory"]
					observed_commodity_index_3_459 = id_index_3_431
					observed_commodity_value_3_460 = observed_commodity_value_2_458[observed_commodity_index_3_459]
					if not ("observed_commodity" in observed_commodity_value_3_460):
						pass
					else:
						observed_commodity_value_4_461 = observed_commodity_value_3_460["observed_commodity"]
						if not (observed_commodity_value_4_461 in observed_commodity_missing_values_24):
							writer_55.write_data_property("https://minmod.isi.edu/resource/observed_commodity", observed_commodity_value_4_461, None)
				
				# Retrieve value of object property: id_document_ref
				id_document_ref_value_0_462 = resource_data_1["MineralSite"]
				id_document_ref_index_1_463 = id_index_1_426
				id_document_ref_value_1_464 = id_document_ref_value_0_462[id_document_ref_index_1_463]
				if not ("mineral_inventory" in id_document_ref_value_1_464):
					pass
				else:
					id_document_ref_value_2_465 = id_document_ref_value_1_464["mineral_inventory"]
					id_document_ref_index_3_466 = id_index_3_431
					id_document_ref_value_3_467 = id_document_ref_value_2_465[id_document_ref_index_3_466]
					if not ("reference" in id_document_ref_value_3_467):
						pass
					else:
						id_document_ref_value_4_468 = id_document_ref_value_3_467["reference"]
						if not ("document" in id_document_ref_value_4_468):
							pass
						else:
							id_document_ref_value_5_469 = id_document_ref_value_4_468["document"]
							if not ("id" in id_document_ref_value_5_469):
								pass
							else:
								id_document_ref_value_6_470 = id_document_ref_value_5_469["id"]
								if writer_55.has_written_record((42, id_document_ref_value_6_470)):
									writer_55.write_object_property("https://minmod.isi.edu/resource/reference", (42, id_document_ref_value_6_470), False, True, False)
				
				# Retrieve value of object property: ore_unit
				ore_unit_value_0_471 = resource_data_1["MineralSite"]
				ore_unit_index_1_472 = id_index_1_426
				ore_unit_value_1_473 = ore_unit_value_0_471[ore_unit_index_1_472]
				if not ("mineral_inventory" in ore_unit_value_1_473):
					pass
				else:
					ore_unit_value_2_474 = ore_unit_value_1_473["mineral_inventory"]
					ore_unit_index_3_475 = id_index_3_431
					ore_unit_value_3_476 = ore_unit_value_2_474[ore_unit_index_3_475]
					if not ("ore" in ore_unit_value_3_476):
						pass
					else:
						ore_unit_value_4_477 = ore_unit_value_3_476["ore"]
						if not ("ore_unit" in ore_unit_value_4_477):
							pass
						else:
							ore_unit_value_5_478 = ore_unit_value_4_477["ore_unit"]
							if writer_55.has_written_record((33, ore_unit_index_1_472, ore_unit_index_3_475)):
								writer_55.write_object_property("https://minmod.isi.edu/resource/ore", (33, ore_unit_index_1_472, ore_unit_index_3_475), False, True, False)
				
				# Retrieve value of object property: grade_unit
				grade_unit_value_0_479 = resource_data_1["MineralSite"]
				grade_unit_index_1_480 = id_index_1_426
				grade_unit_value_1_481 = grade_unit_value_0_479[grade_unit_index_1_480]
				if not ("mineral_inventory" in grade_unit_value_1_481):
					pass
				else:
					grade_unit_value_2_482 = grade_unit_value_1_481["mineral_inventory"]
					grade_unit_index_3_483 = id_index_3_431
					grade_unit_value_3_484 = grade_unit_value_2_482[grade_unit_index_3_483]
					if not ("grade" in grade_unit_value_3_484):
						pass
					else:
						grade_unit_value_4_485 = grade_unit_value_3_484["grade"]
						if not ("grade_unit" in grade_unit_value_4_485):
							pass
						else:
							grade_unit_value_5_486 = grade_unit_value_4_485["grade_unit"]
							if writer_55.has_written_record((34, grade_unit_index_1_480, grade_unit_index_3_483)):
								writer_55.write_object_property("https://minmod.isi.edu/resource/grade", (34, grade_unit_index_1_480, grade_unit_index_3_483), False, True, False)
				
				# Retrieve value of object property: cutoff_grade_unit
				cutoff_grade_unit_value_0_487 = resource_data_1["MineralSite"]
				cutoff_grade_unit_index_1_488 = id_index_1_426
				cutoff_grade_unit_value_1_489 = cutoff_grade_unit_value_0_487[cutoff_grade_unit_index_1_488]
				if not ("mineral_inventory" in cutoff_grade_unit_value_1_489):
					pass
				else:
					cutoff_grade_unit_value_2_490 = cutoff_grade_unit_value_1_489["mineral_inventory"]
					cutoff_grade_unit_index_3_491 = id_index_3_431
					cutoff_grade_unit_value_3_492 = cutoff_grade_unit_value_2_490[cutoff_grade_unit_index_3_491]
					if not ("cutoff_grade" in cutoff_grade_unit_value_3_492):
						pass
					else:
						cutoff_grade_unit_value_4_493 = cutoff_grade_unit_value_3_492["cutoff_grade"]
						if not ("grade_unit" in cutoff_grade_unit_value_4_493):
							pass
						else:
							cutoff_grade_unit_value_5_494 = cutoff_grade_unit_value_4_493["grade_unit"]
							if writer_55.has_written_record((32, cutoff_grade_unit_index_1_488, cutoff_grade_unit_index_3_491)):
								writer_55.write_object_property("https://minmod.isi.edu/resource/cutoff_grade", (32, cutoff_grade_unit_index_1_488, cutoff_grade_unit_index_3_491), False, True, False)
				
				# Retrieve value of object property: category
				category_value_0_495 = resource_data_1["MineralSite"]
				category_index_1_496 = id_index_1_426
				category_value_1_497 = category_value_0_495[category_index_1_496]
				if not ("mineral_inventory" in category_value_1_497):
					pass
				else:
					category_value_2_498 = category_value_1_497["mineral_inventory"]
					category_index_3_499 = id_index_3_431
					category_value_3_500 = category_value_2_498[category_index_3_499]
					if not ("category" in category_value_3_500):
						pass
					else:
						category_value_4_501 = category_value_3_500["category"]
						start_502 = 0
						end_503 = len(category_value_4_501)
						for category_index_5_504 in range(start_502, end_503):
							category_value_5_505 = category_value_4_501[category_index_5_504]
							if writer_55.has_written_record(category_value_5_505):
								writer_55.write_object_property("https://minmod.isi.edu/resource/category", category_value_5_505, False, False, False)
				
				writer_55.end_record()
	
	# Transform records of class mndr:MineralSite:1
	id_mineral_site_value_0_506 = resource_data_1["MineralSite"]
	start_507 = 0
	end_508 = len(id_mineral_site_value_0_506)
	for id_mineral_site_index_1_509 in range(start_507, end_508):
		id_mineral_site_value_1_510 = id_mineral_site_value_0_506[id_mineral_site_index_1_509]
		id_mineral_site_value_2_511 = id_mineral_site_value_1_510["id"]
		writer_55.begin_record("https://minmod.isi.edu/resource/MineralSite", id_mineral_site_value_2_511, False, False)
		
		# Retrieve value of data property: id_mineral_site
		writer_55.write_data_property("https://minmod.isi.edu/resource/id", id_mineral_site_value_2_511, None)
		
		# Retrieve value of data property: name_mineral_site
		name_mineral_site_value_0_512 = resource_data_1["MineralSite"]
		name_mineral_site_index_1_513 = id_mineral_site_index_1_509
		name_mineral_site_value_1_514 = name_mineral_site_value_0_512[name_mineral_site_index_1_513]
		if not ("name" in name_mineral_site_value_1_514):
			pass
		else:
			name_mineral_site_value_2_515 = name_mineral_site_value_1_514["name"]
			if not (name_mineral_site_value_2_515 in name_mineral_site_missing_values_2):
				writer_55.write_data_property("https://minmod.isi.edu/resource/name", name_mineral_site_value_2_515, None)
		
		# Retrieve value of data property: source_mineral_site
		source_mineral_site_value_0_516 = resource_data_1["MineralSite"]
		source_mineral_site_index_1_517 = id_mineral_site_index_1_509
		source_mineral_site_value_1_518 = source_mineral_site_value_0_516[source_mineral_site_index_1_517]
		source_mineral_site_value_2_519 = source_mineral_site_value_1_518["source_id"]
		writer_55.write_data_property("https://minmod.isi.edu/resource/source_id", source_mineral_site_value_2_519, None)
		
		# Retrieve value of data property: record_mineral_site
		record_mineral_site_value_0_520 = resource_data_1["MineralSite"]
		record_mineral_site_index_1_521 = id_mineral_site_index_1_509
		record_mineral_site_value_1_522 = record_mineral_site_value_0_520[record_mineral_site_index_1_521]
		record_mineral_site_value_2_523 = record_mineral_site_value_1_522["record_id"]
		writer_55.write_data_property("https://minmod.isi.edu/resource/record_id", record_mineral_site_value_2_523, None)
		
		# Retrieve value of data property: mineral_site_type
		mineral_site_type_value_0_524 = resource_data_1["MineralSite"]
		mineral_site_type_index_1_525 = id_mineral_site_index_1_509
		mineral_site_type_value_1_526 = mineral_site_type_value_0_524[mineral_site_type_index_1_525]
		if not ("site_type" in mineral_site_type_value_1_526):
			pass
		else:
			mineral_site_type_value_2_527 = mineral_site_type_value_1_526["site_type"]
			if True:
				writer_55.write_data_property("https://minmod.isi.edu/resource/site_type", mineral_site_type_value_2_527, None)
		
		# Retrieve value of data property: mineral_site_rank
		mineral_site_rank_value_0_528 = resource_data_1["MineralSite"]
		mineral_site_rank_index_1_529 = id_mineral_site_index_1_509
		mineral_site_rank_value_1_530 = mineral_site_rank_value_0_528[mineral_site_rank_index_1_529]
		if not ("site_rank" in mineral_site_rank_value_1_530):
			pass
		else:
			mineral_site_rank_value_2_531 = mineral_site_rank_value_1_530["site_rank"]
			if True:
				writer_55.write_data_property("https://minmod.isi.edu/resource/site_rank", mineral_site_rank_value_2_531, None)
		
		# Retrieve value of object property: id_deposit_type_candidate
		id_deposit_type_candidate_value_0_532 = resource_data_1["MineralSite"]
		id_deposit_type_candidate_index_1_533 = id_mineral_site_index_1_509
		id_deposit_type_candidate_value_1_534 = id_deposit_type_candidate_value_0_532[id_deposit_type_candidate_index_1_533]
		if not ("deposit_type_candidate" in id_deposit_type_candidate_value_1_534):
			pass
		else:
			id_deposit_type_candidate_value_2_535 = id_deposit_type_candidate_value_1_534["deposit_type_candidate"]
			start_536 = 0
			end_537 = len(id_deposit_type_candidate_value_2_535)
			for id_deposit_type_candidate_index_3_538 in range(start_536, end_537):
				id_deposit_type_candidate_value_3_539 = id_deposit_type_candidate_value_2_535[id_deposit_type_candidate_index_3_538]
				if not ("id" in id_deposit_type_candidate_value_3_539):
					pass
				else:
					id_deposit_type_candidate_value_4_540 = id_deposit_type_candidate_value_3_539["id"]
					if writer_55.has_written_record(id_deposit_type_candidate_value_4_540):
						writer_55.write_object_property("https://minmod.isi.edu/resource/deposit_type_candidate", id_deposit_type_candidate_value_4_540, False, False, False)
		
		# Retrieve value of object property: location_info_country
		location_info_country_value_0_541 = resource_data_1["MineralSite"]
		location_info_country_index_1_542 = id_mineral_site_index_1_509
		location_info_country_value_1_543 = location_info_country_value_0_541[location_info_country_index_1_542]
		if not ("location_info" in location_info_country_value_1_543):
			pass
		else:
			location_info_country_value_2_544 = location_info_country_value_1_543["location_info"]
			if not ("country" in location_info_country_value_2_544):
				pass
			else:
				location_info_country_value_3_545 = location_info_country_value_2_544["country"]
				if writer_55.has_written_record((14, location_info_country_index_1_542)):
					writer_55.write_object_property("https://minmod.isi.edu/resource/location_info", (14, location_info_country_index_1_542), False, True, False)
		
		# Retrieve value of object property: id
		id_value_0_546 = resource_data_1["MineralSite"]
		id_index_1_547 = id_mineral_site_index_1_509
		id_value_1_548 = id_value_0_546[id_index_1_547]
		if not ("mineral_inventory" in id_value_1_548):
			pass
		else:
			id_value_2_549 = id_value_1_548["mineral_inventory"]
			start_550 = 0
			end_551 = len(id_value_2_549)
			for id_index_3_552 in range(start_550, end_551):
				id_value_3_553 = id_value_2_549[id_index_3_552]
				id_value_4_554 = id_value_3_553["id"]
				if writer_55.has_written_record(id_value_4_554):
					writer_55.write_object_property("https://minmod.isi.edu/resource/mineral_inventory", id_value_4_554, False, False, False)
		
		writer_55.end_record()
	
	# Transform records of class mndr:GeologyInfo:1
	geology_info_unit_name_value_0_555 = resource_data_1["MineralSite"]
	start_556 = 0
	end_557 = len(geology_info_unit_name_value_0_555)
	for geology_info_unit_name_index_1_558 in range(start_556, end_557):
		geology_info_unit_name_value_1_559 = geology_info_unit_name_value_0_555[geology_info_unit_name_index_1_558]
		if not ("geology_info" in geology_info_unit_name_value_1_559):
			continue
		else:
			geology_info_unit_name_value_2_560 = geology_info_unit_name_value_1_559["geology_info"]
			if not ("unit_name" in geology_info_unit_name_value_2_560):
				continue
			else:
				geology_info_unit_name_value_3_561 = geology_info_unit_name_value_2_560["unit_name"]
				writer_55.begin_record("https://minmod.isi.edu/resource/GeologyInfo", (20, geology_info_unit_name_index_1_558), True, False)
				
				# Retrieve value of data property: geology_info_unit_name
				if not (geology_info_unit_name_value_3_561 in geology_info_unit_name_missing_values_17):
					writer_55.write_data_property("https://minmod.isi.edu/resource/unit_name", geology_info_unit_name_value_3_561, None)
				
				# Retrieve value of data property: geology_info_age
				geology_info_age_value_0_562 = resource_data_1["MineralSite"]
				geology_info_age_index_1_563 = geology_info_unit_name_index_1_558
				geology_info_age_value_1_564 = geology_info_age_value_0_562[geology_info_age_index_1_563]
				if not ("geology_info" in geology_info_age_value_1_564):
					pass
				else:
					geology_info_age_value_2_565 = geology_info_age_value_1_564["geology_info"]
					if not ("age" in geology_info_age_value_2_565):
						pass
					else:
						geology_info_age_value_3_566 = geology_info_age_value_2_565["age"]
						if not (geology_info_age_value_3_566 in geology_info_age_missing_values_16):
							writer_55.write_data_property("https://minmod.isi.edu/resource/age", geology_info_age_value_3_566, None)
				
				# Retrieve value of data property: geology_info_lithology
				geology_info_lithology_value_0_567 = resource_data_1["MineralSite"]
				geology_info_lithology_index_1_568 = geology_info_unit_name_index_1_558
				geology_info_lithology_value_1_569 = geology_info_lithology_value_0_567[geology_info_lithology_index_1_568]
				if not ("geology_info" in geology_info_lithology_value_1_569):
					pass
				else:
					geology_info_lithology_value_2_570 = geology_info_lithology_value_1_569["geology_info"]
					if not ("lithology" in geology_info_lithology_value_2_570):
						pass
					else:
						geology_info_lithology_value_3_571 = geology_info_lithology_value_2_570["lithology"]
						if not (geology_info_lithology_value_3_571 in geology_info_lithology_missing_values_19):
							writer_55.write_data_property("https://minmod.isi.edu/resource/lithology", geology_info_lithology_value_3_571, None)
				
				# Retrieve value of data property: geology_info_comments
				geology_info_comments_value_0_572 = resource_data_1["MineralSite"]
				geology_info_comments_index_1_573 = geology_info_unit_name_index_1_558
				geology_info_comments_value_1_574 = geology_info_comments_value_0_572[geology_info_comments_index_1_573]
				if not ("geology_info" in geology_info_comments_value_1_574):
					pass
				else:
					geology_info_comments_value_2_575 = geology_info_comments_value_1_574["geology_info"]
					if not ("comments" in geology_info_comments_value_2_575):
						pass
					else:
						geology_info_comments_value_3_576 = geology_info_comments_value_2_575["comments"]
						if not (geology_info_comments_value_3_576 in geology_info_comments_missing_values_22):
							writer_55.write_data_property("https://minmod.isi.edu/resource/comments", geology_info_comments_value_3_576, None)
				
				# Retrieve value of data property: geology_info_description
				geology_info_description_value_0_577 = resource_data_1["MineralSite"]
				geology_info_description_index_1_578 = geology_info_unit_name_index_1_558
				geology_info_description_value_1_579 = geology_info_description_value_0_577[geology_info_description_index_1_578]
				if not ("geology_info" in geology_info_description_value_1_579):
					pass
				else:
					geology_info_description_value_2_580 = geology_info_description_value_1_579["geology_info"]
					if not ("description" in geology_info_description_value_2_580):
						pass
					else:
						geology_info_description_value_3_581 = geology_info_description_value_2_580["description"]
						if not (geology_info_description_value_3_581 in geology_info_description_missing_values_18):
							writer_55.write_data_property("https://minmod.isi.edu/resource/description", geology_info_description_value_3_581, None)
				
				# Retrieve value of data property: geology_info_process
				geology_info_process_value_0_582 = resource_data_1["MineralSite"]
				geology_info_process_index_1_583 = geology_info_unit_name_index_1_558
				geology_info_process_value_1_584 = geology_info_process_value_0_582[geology_info_process_index_1_583]
				if not ("geology_info" in geology_info_process_value_1_584):
					pass
				else:
					geology_info_process_value_2_585 = geology_info_process_value_1_584["geology_info"]
					if not ("process" in geology_info_process_value_2_585):
						pass
					else:
						geology_info_process_value_3_586 = geology_info_process_value_2_585["process"]
						if not (geology_info_process_value_3_586 in geology_info_process_missing_values_20):
							writer_55.write_data_property("https://minmod.isi.edu/resource/process", geology_info_process_value_3_586, None)
				
				writer_55.end_record()
	
	output_587 = writer_55.write_to_string()
	return output_587

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))