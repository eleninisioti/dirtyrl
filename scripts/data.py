import matplotlib.pyplot as plt
import numpy as np
gpu = ['0.0020081261263953315', '0.0020240038313516758', '0.0020342161023473165', '0.00204189844358535', '0.002049040516685037', '0.002066556035086166', '0.002077043514142091', '0.0020830542228438636', '0.0020914250197035544', '0.0020994173579745824', '0.0021148260504334836', '0.002121765800144361', '0.0021284310817718506', '0.0021343099360770367', '0.0021482862598017644', '0.0021590146496891977', '0.0021643404149517573', '0.0021703033787863596', '0.0021770197357794253', '0.002191998908519745', '0.002197220960465988', '0.0022024117217344396', '0.002207407701362684', '0.002219873354985164', '0.002228450495856149', '0.0022330210906154704', '0.0022382647389563443', '0.0022453284440217196', '0.002257943170879959', '0.00226286499933763', '0.002267090314143413', '0.0022723374388047626', '0.0022851717788561258', '0.002290543796723349', '0.002294648779993472', '0.0022983671611753005', '0.002305869265499278', '0.0023160325672666906', '0.0023200025618577203', '0.002323650010426839', '0.0023280861298900007', '0.0023401738874247817', '0.002343053457213611', '0.0023468928375551777', '0.002349887102127075', '0.00235731237653702', '0.0023652271661232776', '0.0023679316882044077', '0.0023705363772636235', '0.002374180498489967', '0.002385020620040311', '0.0023870311560052816', '0.002390343943932899', '0.0023931566619161348', '0.0024004961932146992', '0.0024078616675208596', '0.00241085410118103', '0.002414414191591567', '0.002417647751115209', '0.0024266235964638845', '0.002429472230004926', '0.002432500372470265', '0.0024342798869926613', '0.002442395935455958', '0.0024460929525309595', '0.002447885663542029', '0.002450889451163156', '0.0024548466737205916', '0.0024622654306808572', '0.0024642821296056113', '0.002466635459306224', '0.0024683659217859567', '0.0024766927996492075', '0.002479697040149144', '0.0024811157334235405', '0.002483329912026723', '0.0024874157784091438', '0.0024937472449073307', '0.0024961503406740583', '0.0024978815257549287', '0.0024997994055659133', '0.0025082157291012046', '0.002509901248604242', '0.0025112510061845545', '0.0025129891872406004', '0.0025187968891787244', '0.002522876818023042', '0.0025249232536270504', '0.0025262689054364987', '0.002528874536121593', '0.002535919993941547', '0.002537459883578988', '0.0025393249740490336', '0.002540716968733689', '0.0025470948478153775', '0.0025502342690121044', '0.002551586702045074', '0.0025535723761226353', '0.0025569441864610382', '0.0025617979764938357', '0.002563011302473795', '0.0025645275849562423', '0.002565820230160906', '0.0025729775804540387', '0.002574597062291326', '0.002575737346885025', '0.002576960707730788', '0.002582367592669548', '0.002584826490866444', '0.002586816379898473', '0.002587530745261627', '0.0025900762217740216', '0.002594951708699755', '0.002595966320676902', '0.0025975041401691927', '0.002598900393563874', '0.002605258020652732', '0.0026069141758812797', '0.0026078279857060416', '0.00260932333946228', '0.0026140333099744805', '0.0026166663807217438', '0.0026177465939169445', '0.0026184076035723966', '0.0026203675874849645', '0.002625573547141066', '0.0026264245705904018', '0.0026280287687595076', '0.0026288390205237286', '0.002634842319715591', '0.0026356651647395997', '0.0026370105878362115', '0.0026383674044004627', '0.0026424592176330424', '0.002644830169234165', '0.0026460625838350365', '0.00264675746205765', '0.002649250506261073', '0.002653696948534822', '0.00265437087579207', '0.002655586759429172', '0.002656377923381221', '0.0026619747176833217', '0.0026634196266531944', '0.0026638803641001385', '0.002664993042439486', '0.0026686950223561426', '0.002670798355027249', '0.0026718765367066497', '0.0026722169637680053', '0.0026747954614234695', '0.002678483254950622', '0.002678835817672664', '0.0026799325718838943', '0.002680810645286073', '0.0026859458745536156', '0.00268731796087595', '0.0026879832644422516', '0.002688902199517733', '0.0026933854818344117', '0.0026948846801187983', '0.0026954536664584453', '0.0026958884368708104', '0.0026985626670180773', '0.002701549647778881', '0.002702176572830696', '0.0027032256425633602', '0.0027044653431061777', '0.00270848905896566', '0.00270910107421875', '0.0027097192143064096', '0.0027104899306145927', '0.0027146500513958835', '0.0027157416437554546', '0.0027162147690268125', '0.0027169683137908576', '0.0027197136294517072', '0.0027221871780794722', '0.002723464463208173', '0.0027241451657735384', '0.002726437250773112', '0.0027299069375482225', '0.0027304348592069212', '0.0027316338311542164', '0.0027320316503632743', '0.0027365473392314483', '0.002737523844179589', '0.0027381457072585377', '0.0027386531218277035', '0.0027424977911843194', '0.0027437808680798293', '0.0027440936039475833', '0.002744993318131555', '0.002747745408628979', '0.0027498685854131523', '0.0027509121091469474', '0.002751329601886901', '0.002753150786427285', '0.0027561535741265956', '0.002756729117461613', '0.002757450667140323', '0.0027581895014918444', '0.0027625194969109848', '0.00276320854710861', '0.002763796333681073', '0.002764315229195815', '0.0027685366100550527', '0.0027691822871565817', '0.00276962144317099', '0.002770499509778516', '0.0027731775639393075', '0.002774907450153403', '0.002775674219424407', '0.0027763872470985464', '0.002778435786295745', '0.0027811864050658972', '0.002781872804718788', '0.0027824228897990796', '0.002783634441752099', '0.0027870962071418763', '0.002787763213794493', '0.0027882139714348396', '0.002788578747129283', '0.0027924892816104385', '0.0027931887517209913', '0.0027942359603308387', '0.002794829292483749', '0.0027982814110718763', '0.002799403991514039', '0.002799850858411481', '0.0028005960853920106', '0.002803397388794483', '0.0028050595693314036', '0.002805438068262331', '0.002806124261068919', '0.0028082508422151396', '0.0028107398015091473', '0.0028113881034671135', '0.0028121329624451064', '0.0028137499697506426', '0.0028165580847553003', '0.0028172746289590873', '0.002817861660346158', '0.0028191099542158623', '0.005851381341494047', '0.005843394787033643', '0.005835091751285285', '0.005829234845027691', '0.005821281951249189', '0.00581343403151541', '0.005806209534676774', '0.005799946909209332', '0.00579177845777334']
gpu_jz = ['0.0018188855912950304', '0.001825450789637682', '0.001832033292356744', '0.0018383927969705491', '0.001844489871754366', '0.0018506755607072697', '0.001856601060121909', '0.0018623114851388065', '0.0018680778112304345', '0.0018737407975726657', '0.001879112020953671', '0.001884680379991946', '0.0018898908989403837', '0.0018947972465068737', '0.0018997754874982332', '0.0019046664933363596', '0.001909433473016798', '0.0019143112508618102', '0.0019190301557984015', '0.0019237012529373168', '0.0019282250003059313', '0.0019327097500071806', '0.0019369706876069597', '0.001941121933551935', '0.0019451346896943592', '0.001949288233271185', '0.0019532505752884338', '0.001957007277894903', '0.001960734223007062', '0.0019645643971183085', '0.0019682768443683245', '0.0019718393491847176', '0.0019753877631330913', '0.0019789276687722456', '0.0019823194400123926', '0.001985705437331364', '0.001989009158224122', '0.0019926214541419076', '0.0019959921616466104', '0.001999234410127004', '0.002002540879998325', '0.0020056984092368456', '0.0020086928925863124', '0.002011583564742919', '0.002014497817993164', '0.0020173739138103666', '0.0020201758512361783', '0.0020230560954660175', '0.0020259393037751665', '0.002028530819599445', '0.002031209033864145', '0.0020337679602883078', '0.002036310785695126', '0.002039084112466271', '0.002041697405002735', '0.002044264274484971', '0.002046855755966075', '0.0020492412335630776', '0.0020516327130708765', '0.0020538889016423908', '0.002056158221359794', '0.002058494635031257', '0.0020607624804223333', '0.0020631029937002395', '0.0020653056720207476', '0.0020674988227347806', '0.0020697973050227783', '0.0020718171113246198', '0.0020737611655420904', '0.002075918534596761', '0.0020780288746814852', '0.002080023627532156', '0.0020820293410930757', '0.0020840278383973355', '0.002085864265503422', '0.0020877849963995125', '0.002089683915399442', '0.002091552794734134', '0.0020934478096991966', '0.002095277251303196', '0.0020971741394967026', '0.002099038536165967', '0.0021008410541557827', '0.0021027491005455577', '0.0021045564376946653', '0.0021063832576016348', '0.002108191525864744', '0.0021100172159217653', '0.002111604944488706', '0.0021133210953544167', '0.0021150295832003765', '0.002116736571456111', '0.002118450603044102', '0.002120116124207946', '0.0021216273198808944', '0.0021233109615065833', '0.002124910201056529', '0.002126362475116601', '0.0021278688521358556', '0.0021293940199746024', '0.0021310720061728967', '0.0021326163378390635', '0.002134151589023611', '0.0021356433565201966', '0.0021370822687406797', '0.0021385684731186076', '0.0021399551814890163', '0.0021414971567214804', '0.002142972324260328', '0.0021443997947793256', '0.00214571237064781', '0.002147131145000458', '0.002148502679686472', '0.002149855291720518', '0.0021512586471361993', '0.002152522743964682', '0.0021538160646022275', '0.002154986585029448', '0.0021562293150916173', '0.00215747340798378', '0.002158700200455699', '0.002159999099108252', '0.002161156401845622', '0.002162352582987617', '0.002163599866774024', '0.00216481626728206', '0.0021660358041956803', '0.002167335740648783', '0.002168484662708483', '0.002169622760727292', '0.0021706799861944117', '0.0021718148094303203', '0.0021730106391817192', '0.0021741703381048185', '0.002175335368444753', '0.0021764621745657036', '0.0021776834973541823', '0.0021788246150410504', '0.0021800148247583815', '0.0021810766610232267', '0.0021820964543528146', '0.002183225924904282', '0.0021842759200810316', '0.002185412399470806', '0.0021864087539248994', '0.0021875027164948726', '0.002188608169555664', '0.0021897165294279134', '0.0021909071035260195', '0.002191899745360665', '0.0021930114603661874']
cpu = ['0.0012875521860004943', '0.0013927922219764896', '0.0015057404213641064', '0.0016009458814348493', '0.001697092586405137', '0.0018012866752092228', '0.001898736011022809', '0.002002543571320447', '0.0020907644716541417', '0.0021773917436599733', '0.002258895978822813', '0.0023393145670061524', '0.0024157509675589942', '0.002493778467178345', '0.0025666008748506243', '0.0026392669901251792', '0.002709595505724248', '0.002783816695213318', '0.002858843203746911', '0.0029255987787246704', '0.002989832545271014', '0.003056742705550848', '0.003129908952898192', '0.0031886811256408693', '0.0032531553041367303', '0.003314953642071418', '0.003375168363624644', '0.003435039063294729', '0.0034936462301726734', '0.0035502622907811945', '0.00360954009949624', '0.0036653189190796443', '0.0037192453283124267', '0.003772427991816872', '0.003824758129534514', '0.00387928994976241', '0.00393257909350925', '0.00398291771290666', '0.004034776218798982', '0.004087234199047088', '0.004134547686773883', '0.004183633032392283', '0.004230660171043582', '0.0042801004513617485', '0.004324963104248047', '0.004371479673991128', '0.0044170879998545005', '0.004462609717622399', '0.004511842441189197', '0.004560838978107159', '0.004604196177184126', '0.004651277401230552', '0.004697010968860827', '0.0047395082605418875', '0.004780153763735736', '0.004824158118051641', '0.004871906014254493', '0.004919097601503566', '0.004959043230084207', '0.0049958863922527855', '0.005032223297349104', '0.005067750816613856', '0.005104393197106314', '0.005148669938246409', '0.005185500787866526', '0.005237538964781042', '0.005273879203666635', '0.005305995696299785', '0.005342126295870582', '0.005379114400545756', '0.0054144834303698', '0.005448508309690576', '0.005482676099328434', '0.0055161429473332', '0.00555355465796686', '0.005586440468445802', '0.005625099854864132', '0.005662358222128469', '0.005693364089390017', '0.00572406944334507', '0.005756067292290445', '0.005791733518058871', '0.005821418209309958', '0.005854405189432749', '0.005883982932928837', '0.0059152290835438005', '0.005945984904637594', '0.005979209274053573', '0.006012941019069513', '0.006045449900627136', '0.006074754444479245', '0.006105801111043886', '0.006132560920164076', '0.006158522482576041', '0.006185535565784999', '0.006216847949407318', '0.006245613661189537', '0.006273264067896297', '0.006297964397089442', '0.006324048123094771', '0.00634959724331429', '0.006377382852218963', '0.006402713224536082', '0.00642828579959662', '0.006455185583475474', '0.006480934913440417', '0.006505300641697358', '0.006532052267105021', '0.006555616868236078', '0.006579753978628861', '0.006602276602340618', '0.0066250446451207', '0.006648093736233489', '0.006670626907004523', '0.006695848266895001', '0.006719449959239181', '0.006741311456951393', '0.006762570868838917', '0.006784472231888891', '0.006820561985969543', '0.0068457858906456484', '0.006867405634115238', '0.006887003971438103', '0.006908747034914353', '0.0069300768340506205', '0.006950060239115965', '0.006968597314208026', '0.006988537856019461', '0.00700912405657426', '0.0070286127045041035', '0.007048229981372707', '0.007067797104142747', '0.007085979266905449', '0.007104267153784493', '0.007119209753080856', '0.0071350738240612875', '0.0071525310788835795', '0.007169362445490076', '0.007189940415560927', '0.007211236482316798', '0.007232004932688372', '0.007251852725003217', '0.007268552022129966', '0.00728511316967862', '0.0073013243685828315', '0.007317174707893777', '0.00733431392514233', '0.007351496417271464', '0.007374172607363572', '0.007393974000474681', '0.007410237766447521', '0.007424960353251161', '0.007442062961185439', '0.007459540983550569', '0.007480969936289686', '0.007500424046637648', '0.00751894561147891', '0.007538209265019713', '0.007553770059322213', '0.007567836741606395', '0.0075837379926467835', '0.0075999263603825215', '0.007616351213965396', '0.007634777094497056', '0.007652865861386669', '0.00766927234525603', '0.007683067417337827', '0.007698269073040255', '0.0077148901248073965', '0.007733217680931092', '0.007750714132035396', '0.007771782638534667', '0.00778747238754755', '0.007803468520247091', '0.007820378851423077', '0.007836260886862874', '0.00785268671967176', '0.007868378151294797', '0.007883972537103308', '0.00789972290809338', '0.00791560810735856', '0.007931608732420069', '0.007950414498042698', '0.007965898795561357', '0.007981914698402837', '0.00799871023346607', '0.008014539224824655', '0.008028805312825673', '0.008042346722131326', '0.008056106573564035', '0.008070442683582377', '0.008085309352944879', '0.008097711263558804', '0.008108978565591965', '0.008125542258349333', '0.008141059826249662', '0.008153393191981401', '0.008165192543173865', '0.008181737354579366', '0.008194476517609187', '0.008207555284703754', '0.008218274790344508', '0.008227173904648097', '0.00824460464464107', '0.008254980948096827', '0.008265819059385286', '0.008276718801737663', '0.008287419608069791', '0.008297890519600839', '0.008309567286228312', '0.008330279564120106', '0.008348326308270024', '0.008363202351352053', '0.008372824197723751', '0.008388418250972942', '0.008399958338286426', '0.008412063771225387', '0.00842263534885125', '0.008433921304434837', '0.008450291004180908', '0.008462466248642171', '0.008477533000194474', '0.008487667528316133', '0.00850022568749754', '0.008516973071801858', '0.008532119921609467', '0.008541786029983421', '0.008551982526655321', '0.008563001844875249', '0.008579300122876322', '0.008588832305558625', '0.008604350679960007', '0.008614153179497765', '0.008624465166383488', '0.008638878003377762', '0.008656411097774023', '0.008667978337886581', '0.008677067156857664', '0.0086938173008563', '0.008703928562253714', '0.00871267677244739', '0.008721175909782788', '0.008730355244302898', '0.00874617647830351', '0.00875687957250155', '0.008766188950626396', '0.008775353988011677', '0.00879007344274986', '0.008800144702105536', '0.00881486365217151', '0.00882568420240166', '0.008834799132433282', '0.008844214504545516', '0.008859067943281757', '0.00887272894062213', '0.00888768430621851', '0.008899284789399506', '0.00891328399139043', '0.008924900537395196', '0.00893445664363749', '0.008943819519361792', '0.008958751576685766', '0.00896878691873467', '0.008979727343071339', '0.00899398069312607', '0.009004813733817525', '0.009013064637307819', '0.0090204555371712', '0.00904225104039583', '0.00905602663721357', '0.009064278119649643', '0.009071984889832409', '0.009080074119162626', '0.009089565618563507', '0.009102786098399632', '0.009110731059245848', '0.009125150462158588', '0.0091346773881486', '0.009143322011554473', '0.00915676441391309', '0.009168095631612635', '0.00917616647251403', '0.009183997049147762', '0.009192403214318412', '0.009205543770202218', '0.00921468641523455', '0.009226866242671208', '0.009236953143840251', '0.009246417808015819', '0.009257069518759443', '0.009264149345156318', '0.009277728089081344', '0.009284732941328361', '0.009290140195326372', '0.009298441546758017', '0.009311602861957348', '0.009318522040344359', '0.009325632899526566', '0.009338816820788824', '0.009346302300377895', '0.0093539414230607', '0.009366144863722836', '0.009373764642536173', '0.00937969533354044', '0.009392302439429543', '0.009400922834564366', '0.009408247103678779', '0.009413585007805186', '0.009418965419337805', '0.00944265123086098', '0.009455403225501174', '0.009470436610129414', '0.009478986794105316', '0.009502133129816974', '0.009530382144300244', '0.009544434787649096', '0.00956785226708996', '0.009587211411802014', '0.009605601574245252', '0.00963283414721489', '0.009654588975216682', '0.009679488674325136', '0.009698410369622204', '0.009727579175835789', '0.009748200064529608', '0.009763612492331143', '0.009790363643913363', '0.009813579531861287', '0.00983212557981533', '0.009858423207445843', '0.009885514467592078', '0.009907712857121402', '0.00993236022769106', '0.009947511256029065', '0.009972605667918561', '0.009986527651548385', '0.010007368777295668', '0.010029816626932062', '0.010046796259845924', '0.01007194047655378', '0.010097483163774722', '0.010118631739751988', '0.01014234216557045', '0.01016569648879879', '0.010187221388536342', '0.010217132380870587', '0.010247345353736252', '0.010266015687278498', '0.010276585279922663', '0.010292251372337342', '0.010302506689129185', '0.010307431722128833', '0.010311105849836496', '0.010315059325112725', '0.010329560657479296', '0.010335870726939735', '0.01033920192936738', '0.010351751274169853', '0.010358698972536926', '0.010363122381947257', '0.010366264567083242', '0.010371422549718106', '0.010384187681680338', '0.010389712783667418', '0.010393775739026874', '0.010396532098808631', '0.010406639713568975', '0.01041423280590347', '0.010418854401212492', '0.010426734369066026', '0.010434874849678937', '0.010439555066349231', '0.010443228975826542', '0.01044596558835538', '0.010456925169452206', '0.010463830727757069', '0.010468823157984527', '0.010473426137428616', '0.010480493285297569', '0.010490026058839716', '0.01049668813268947', '0.010507060950452632', '0.010512303414664052', '0.010517847879179592', '0.010527476554788568', '0.010534023026028416', '0.010537873171126307', '0.010540961974196964', '0.010547120565544568', '0.010563221078730645', '0.010570517895834209', '0.010575205913034536', '0.010577817277222809', '0.010589169308103087', '0.010594416656996074', '0.010597087216477435', '0.010599331121524674', '0.01060869617591842', '0.010616170979242981', '0.010619603797793389', '0.0106228738316875', '0.01062554301265859', '0.010635949805656575', '0.010641118748128908', '0.010643714958859473', '0.010646826993781352', '0.010657292106557921', '0.01066285927227286', '0.010668526971754608', '0.01067865680431833', '0.010684679749541274', '0.010687724138178476', '0.010690243034769023', '0.010701037635687392', '0.010707523488998413', '0.010712082453793095', '0.010723359044648752', '0.010728524432124862', '0.01073215856294116', '0.010735400279998778', '0.010737721255677428', '0.010749608215107861', '0.010767711844643353']
cpu = [float(el) for el in cpu]
gpu = [float(el) for el in gpu]
gpu_jz = [float(el) for el in gpu_jz]

if __name__ == "__main__":
    print(len(gpu), len(cpu), len(gpu_jz))
    plt.plot(range(len(gpu)), gpu, label="gpu")
    plt.plot(range(len(gpu_jz)), gpu_jz, label="gpu_jz")
    plt.plot(range(len(cpu)), cpu, label="cpu")
    # min_value = float(min([min(gpu), min(cpu)])
    # max_value = max([max(gpu), max(cpu)])
    #plt.xticks(np.arange(min_value, max_value, (max_value-min_value)/10),np.arange(min_value, max_value, (max_value-min_value)/10) )
    plt.legend()
    #plt.show()
    plt.savefig("time.png")