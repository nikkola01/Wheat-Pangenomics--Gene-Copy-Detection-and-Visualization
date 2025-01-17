import plotly.graph_objs as go
from random import randint

df = {'TraesCS1A03G0000600.1': [('95906', '104903'), ('102794', '122504'), ('162313', '162609'), ('269472', '289602'), ('270605', '272936'), ('403455', '403751')], 'TraesCS1A03G0001300.1': [('169592', '169969'), ('297266', '297652'), ('326099', '326518')], 'TraesCS1A03G0007700.1': [('1946022', '1947181'), ('1946792', '1947917')], 'TraesCS1A03G0008100.1': [('2058764', '2060237'), ('2058764', '2060237'), ('2058909', '2060171'), ('2058909', '2060171'), ('2058909', '2060171'), ('2058909', '2060171')], 'TraesCS1A03G0014300.1': [('3927688', '3931188'), ('3927688', '3931514')], 'TraesCS1A03G0020400.1': [('5018187', '5019044'), ('5026172', '5027029')], 'TraesCS1A03G0022200.1': [('5551274', '5553366'), ('6671158', '6674613'), ('6690823', '6691371'), ('7519840', '7524507')], 'TraesCS1A03G0029400.1': [('8081207', '8081419'), ('8082307', '8082522')], 'TraesCS1A03G0051100.1': [('12415347', '12415641'), ('505722294', '505722588')], 'TraesCS1A03G0056700.1': [('13551171', '13551368'), ('13611381', '13611578')], 'TraesCS1A03G0061400.1': [('14121494', '14121709'), ('14121494', '14121709')], 'TraesCS1A03G0097300.1': [('24499649', '24499840'), ('280308885', '280309076')], 'TraesCS1A03G0099500.1': [('24723932', '24724480'), ('74217859', '74218407')], 'TraesCS1A03G0110000.1': [('29460953', '29462241'), ('239599939', '239601357')], 'TraesCS1A03G0152800.1': [('45529366', '45530134'), ('45650172', '45650660')], 'TraesCS1A03G0175100.1': [('56515146', '56515932'), ('111623683', '111624466')], 'TraesCS1A03G0183700.1': [('60855174', '60855971'), ('60965417', '60966214')], 'TraesCS1A03G0194200.1': [('65244320', '65244631'), ('363673465', '363674119'), ('458400079', '458400830'), ('486592383', '486593005'), ('486594228', '486594818'), ('489141745', '489142309'), ('489144333', '489144943'), ('489177368', '489177929'), ('491971291', '491971919'), ('492310503', '492311024'), ('543092120', '543092808'), ('543207782', '543208415'), ('545665859', '545666387')], 'TraesCS1A03G0203000.1': [('70360679', '70361182'), ('184093165', '184093562'), ('360686424', '360686822')], 'TraesCS1A03G0222900.1': [('86781070', '86781606'), ('86918267', '86918803')], 'TraesCS1A03G0240100.1': [('97289846', '97290927'), ('97762258', '97763148')], 'TraesCS1A03G0255200.1': [('103177381', '103178256'), ('565374066', '565376066'), ('565377963', '565378692')], 'TraesCS1A03G0375000.1': [('239958271', '239958648'), ('240003568', '240003945'), ('280294439', '280294816')], 'TraesCS1A03G0375100.1': [('239958693', '239959049'), ('240003990', '240004346')], 'TraesCS1A03G0400900.1': [('257904511', '257904762'), ('556470279', '556470530')], 'TraesCS1A03G0437000.1': [('292340783', '292342406'), ('520690110', '520692829')], 'TraesCS1A03G0510800.1': [('345741224', '345741685'), ('402617504', '402617962'), ('402887825', '402888554')], 'TraesCS1A03G0539400.1': [('364471305', '364473173'), ('364495372', '364497378')], 'TraesCS1A03G0586400.1': [('396120548', '396121213'), ('396208930', '396209709')], 'TraesCS1A03G0586500.1': [('396158158', '396158908'), ('396242923', '396243294')], 'TraesCS1A03G0595700.1': [('402622538', '402624074'), ('402636150', '402636799'), ('458397396', '458398630'), ('470264663', '470265073'), ('543067852', '543068600'), ('543129531', '543130274'), ('543210281', '543210977'), ('543916303', '543916713'), ('544104074', '544104804')], 'TraesCS1A03G0618600.1': [('425019156', '425020165'), ('425144696', '425145749'), ('425317649', '425318633'), ('425448612', '425449623')], 'TraesCS1A03G0650900.1': [('445978639', '445979848'), ('448022165', '448023418')], 'TraesCS1A03G0663000.1': [('453793375', '453796206'), ('502052638', '502056041')], 'TraesCS1A03G0692600.1': [('470075343', '470077375'), ('470125991', '470128116')], 'TraesCS1A03G0785700.1': [('509778023', '509778385'), ('509805920', '509806282'), ('509837130', '509837492')], 'TraesCS1A03G0790000.1': [('511205652', '511207137'), ('511279066', '511280511')], 'TraesCS1A03G0804000.1': [('516360646', '516361976'), ('516621661', '516622991'), ('516894819', '516896149')], 'TraesCS1A03G0804200.1': [('516530133', '516530447'), ('516785077', '516788666')], 'TraesCS1A03G0831000.1': [('524683902', '524685979'), ('526827769', '526829635')], 'TraesCS1A03G0850600.1': [('534479119', '534482138'), ('549141481', '549144412')], 'TraesCS1A03G0863800.1': [('538124787', '538131562'), ('538124860', '538131617')], 'TraesCS1A03G0864000.1': [('538134328', '538136597'), ('538134490', '538136337')], 'TraesCS1A03G0881800.1': [('543913915', '543914376'), ('547926796', '547927257'), ('547930855', '547931316'), ('559083373', '559084247')], 'TraesCS1A03G0908100.1': [('551561988', '551562284'), ('551586191', '551586484')], 'TraesCS1A03G0912500.1': [('552560240', '552560455'), ('552594895', '552595990')], 'TraesCS1A03G0921000.1': [('554092536', '554093506'), ('554112931', '554113603')], 'TraesCS1A03G0979300.1': [('567217607', '567218100'), ('567281783', '567282274')], 'TraesCS1A03G0990900.1': [('571592142', '571593215'), ('571859081', '571859347')], 'TraesCS1A03G1018400.1': [('578988463', '578989036'), ('579006934', '579007507')], 'TraesCS1A03G1023000.1': [('579898272', '579898901'), ('579961480', '579962172')]}
nameDF= {'TraesCS1A03G0000600.1': ['TraesCS1A03G0000800.1', 'TraesCS1A03G0001200.1', 'TraesCS1A03G0001700.1', 'TraesCS1A03G0001800.1', 'TraesCS1A03G0003200.1'], 'TraesCS1A03G0001300.1': ['TraesCS1A03G0002400.1', 'TraesCS1A03G0002800.1'], 'TraesCS1A03G0007700.1': ['TraesCS1A03G0007800.1'], 'TraesCS1A03G0008100.1': ['TraesCS1A03G0008200.1', 'TraesCS1A03G0008300.1', 'TraesCS1A03G0008400.1', 'TraesCS1A03G0008500.1', 'TraesCS1A03G0008600.1'], 'TraesCS1A03G0014300.1': ['TraesCS1A03G0014400.1'], 'TraesCS1A03G0020400.1': ['TraesCS1A03G0020500.1'], 'TraesCS1A03G0022200.1': ['TraesCS1A03G0024600.1', 'TraesCS1A03G0024700.1', 'TraesCS1A03G0027700.1'], 'TraesCS1A03G0029400.1': ['TraesCS1A03G0029500.1'], 'TraesCS1A03G0051100.1': ['TraesCS1A03G0775200.1'], 'TraesCS1A03G0056700.1': ['TraesCS1A03G0057700.1'], 'TraesCS1A03G0061400.1': ['TraesCS1A03G0061500.1'], 'TraesCS1A03G0097300.1': ['TraesCS1A03G0423200.1'], 'TraesCS1A03G0099500.1': ['TraesCS1A03G0208300.1'], 'TraesCS1A03G0110000.1': ['TraesCS1A03G0374500.1'], 'TraesCS1A03G0152800.1': ['TraesCS1A03G0152900.1'], 'TraesCS1A03G0175100.1': ['TraesCS1A03G0266400.1'], 'TraesCS1A03G0183700.1': ['TraesCS1A03G0184800.1'], 'TraesCS1A03G0194200.1': ['TraesCS1A03G0538100.1', 'TraesCS1A03G0669100.1', 'TraesCS1A03G0723200.1', 'TraesCS1A03G0723300.1', 'TraesCS1A03G0730200.1', 'TraesCS1A03G0730300.1', 'TraesCS1A03G0730400.1', 'TraesCS1A03G0737200.1', 'TraesCS1A03G0737600.1', 'TraesCS1A03G0878900.1', 'TraesCS1A03G0879500.1', 'TraesCS1A03G0885400.1'], 'TraesCS1A03G0203000.1': ['TraesCS1A03G0337700.1', 'TraesCS1A03G0533500.1'], 'TraesCS1A03G0222900.1': ['TraesCS1A03G0223100.1'], 'TraesCS1A03G0240100.1': ['TraesCS1A03G0241500.1'], 'TraesCS1A03G0255200.1': ['TraesCS1A03G0969800.1', 'TraesCS1A03G0969900.1'], 'TraesCS1A03G0375000.1': ['TraesCS1A03G0376400.1', 'TraesCS1A03G0422500.1'], 'TraesCS1A03G0375100.1': ['TraesCS1A03G0376500.1'], 'TraesCS1A03G0400900.1': ['TraesCS1A03G0930900.1'], 'TraesCS1A03G0437000.1': ['TraesCS1A03G0818500.1'], 'TraesCS1A03G0510800.1': ['TraesCS1A03G0595600.1', 'TraesCS1A03G0596300.1'], 'TraesCS1A03G0539400.1': ['TraesCS1A03G0539500.1'], 'TraesCS1A03G0586400.1': ['TraesCS1A03G0586800.1'], 'TraesCS1A03G0586500.1': ['TraesCS1A03G0586900.1'], 'TraesCS1A03G0595700.1': ['TraesCS1A03G0596000.1', 'TraesCS1A03G0669000.1', 'TraesCS1A03G0693100.1', 'TraesCS1A03G0878800.1', 'TraesCS1A03G0879000.1', 'TraesCS1A03G0879600.1', 'TraesCS1A03G0881900.1', 'TraesCS1A03G0882500.1'], 'TraesCS1A03G0618600.1': ['TraesCS1A03G0618700.1', 'TraesCS1A03G0618800.1', 'TraesCS1A03G0618900.1'], 'TraesCS1A03G0650900.1': ['TraesCS1A03G0654700.1'], 'TraesCS1A03G0663000.1': ['TraesCS1A03G0768600.1'], 'TraesCS1A03G0692600.1': ['TraesCS1A03G0692700.1'], 'TraesCS1A03G0785700.1': ['TraesCS1A03G0786100.1', 'TraesCS1A03G0786500.1'], 'TraesCS1A03G0790000.1': ['TraesCS1A03G0790200.1'], 'TraesCS1A03G0804000.1': ['TraesCS1A03G0804800.1', 'TraesCS1A03G0805500.1'], 'TraesCS1A03G0804200.1': ['TraesCS1A03G0805000.1'], 'TraesCS1A03G0831000.1': ['TraesCS1A03G0832400.1'], 'TraesCS1A03G0850600.1': ['TraesCS1A03G0897100.1'], 'TraesCS1A03G0863800.1': ['TraesCS1A03G0863900.1'], 'TraesCS1A03G0864000.1': ['TraesCS1A03G0864100.1'], 'TraesCS1A03G0881800.1': ['TraesCS1A03G0893900.1', 'TraesCS1A03G0894000.1', 'TraesCS1A03G0948000.1'], 'TraesCS1A03G0908100.1': ['TraesCS1A03G0908200.1'], 'TraesCS1A03G0912500.1': ['TraesCS1A03G0912900.1'], 'TraesCS1A03G0921000.1': ['TraesCS1A03G0921100.1'], 'TraesCS1A03G0979300.1': ['TraesCS1A03G0979900.1'], 'TraesCS1A03G0990900.1': ['TraesCS1A03G0991600.1'], 'TraesCS1A03G1018400.1': ['TraesCS1A03G1018600.1'], 'TraesCS1A03G1023000.1': ['TraesCS1A03G1023200.1']}

graphName = "Triticum aestivum Chromosome 1A Ortholog Groups"

# generate random colors for each group
colors = []
for i in range(len(df) + 1):
    colors.append('#%06X' % randint(0, 0xFFFFFF))


# function to convert hex color code to rgba color code with alpha value
def hex_to_rgba(hex_color, alpha):
    rgba_color = tuple(int(hex_color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)
    return rgba_color


# create the figure object
fig = go.Figure()

# set the height of the bars
bar_height = 10

# loop through each group in the dataframe
for group, ranges, c in zip(df.keys(), df.values(), colors):
    x_values = []
    hp = 'f"{group}'

    # get the x value for the middle of each range
    for start, end in ranges:
        x_values.append((int(start) + int(end)) / 2)

    # add start and end values to hover text
    hp += '<br>Start: %{' + start + '}<br>End: %{' + end + '}"'

    # add a bar trace to the figure
    fig.add_trace(
        go.Bar(x=x_values, y=[bar_height] * len(ranges), width=[int(end) - int(start) for start, end in ranges],
               marker_color=f'rgba{hex_to_rgba(c, 0.7)}', name=group,
               hovertemplate='Group = ' + group + ' ' + str(nameDF[group]))
    )

# update the y-axis settings
fig.update_yaxes(visible=False, showticklabels=False, fixedrange=True, range=[0, 1])

# update the layout settings
fig.update_layout(title_text=graphName, title_x=0.5, barmode='group', plot_bgcolor='white', )

# show the figure
fig.show()
