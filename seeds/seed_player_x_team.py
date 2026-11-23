from app.database import SessionLocal
from entities.player_x_team import PlayerXTeam
from entities.player import Player
from entities.team import Team

db = SessionLocal()

relations = [

    # =========================
    # AMIGOS_UNIDOS (team_id=3)
    # =========================

    PlayerXTeam(player_id=39277840, team_id=3, active=True),
    PlayerXTeam(player_id=47886716, team_id=3, active=True),
    PlayerXTeam(player_id=45397849, team_id=3, active=True),
    PlayerXTeam(player_id=38146730, team_id=3, active=True),
    PlayerXTeam(player_id=43209788, team_id=3, active=True),
    PlayerXTeam(player_id=48115228, team_id=3, active=True),
    PlayerXTeam(player_id=43015460, team_id=3, active=True),
    PlayerXTeam(player_id=36780619, team_id=3, active=True),
    PlayerXTeam(player_id=42720185, team_id=3, active=True),
    PlayerXTeam(player_id=47336034, team_id=3, active=True),
    PlayerXTeam(player_id=38292696, team_id=3, active=True),
    PlayerXTeam(player_id=43596410, team_id=3, active=True),
    PlayerXTeam(player_id=45540229, team_id=3, active=True),
    PlayerXTeam(player_id=42434248, team_id=3, active=True),
    PlayerXTeam(player_id=45579180, team_id=3, active=True),
    PlayerXTeam(player_id=46361008, team_id=3, active=True),
    PlayerXTeam(player_id=47008531, team_id=3, active=True),
    PlayerXTeam(player_id=43906828, team_id=3, active=True),
    PlayerXTeam(player_id=46631126, team_id=3, active=True),
    PlayerXTeam(player_id=48482535, team_id=3, active=True),
    PlayerXTeam(player_id=48882549, team_id=3, active=True),

    # ======================
    # DEFENSORES (team_id=1)
    # ======================

    PlayerXTeam(player_id=43186449, team_id=1, active=True),
    PlayerXTeam(player_id=43798859, team_id=1, active=True),
    PlayerXTeam(player_id=35333308, team_id=1, active=True),
    PlayerXTeam(player_id=46631017, team_id=1, active=True),
    PlayerXTeam(player_id=39787209, team_id=1, active=True),
    PlayerXTeam(player_id=40882934, team_id=1, active=True),
    PlayerXTeam(player_id=41987283, team_id=1, active=True),
    PlayerXTeam(player_id=35180182, team_id=1, active=True),
    PlayerXTeam(player_id=38836907, team_id=1, active=True),
    PlayerXTeam(player_id=42573130, team_id=1, active=True),
    PlayerXTeam(player_id=45916332, team_id=1, active=True),
    PlayerXTeam(player_id=41717600, team_id=1, active=True),
    PlayerXTeam(player_id=40095865, team_id=1, active=True),
    PlayerXTeam(player_id=45811162, team_id=1, active=True),
    PlayerXTeam(player_id=38732687, team_id=1, active=True),
    PlayerXTeam(player_id=47234069, team_id=1, active=True),
    PlayerXTeam(player_id=41216474, team_id=1, active=True),
    PlayerXTeam(player_id=35796834, team_id=1, active=True),
    PlayerXTeam(player_id=45916398, team_id=1, active=True),
    PlayerXTeam(player_id=45292917, team_id=1, active=True),
    PlayerXTeam(player_id=38836911, team_id=1, active=True),

    # ======================
    # LOS_SANTOS (team_id=6)
    # ======================

    PlayerXTeam(player_id=36386029, team_id=6, active=True),
    PlayerXTeam(player_id=46631080, team_id=6, active=True),
    PlayerXTeam(player_id=36361764, team_id=6, active=True),
    PlayerXTeam(player_id=37373967, team_id=6, active=True),
    PlayerXTeam(player_id=41987379, team_id=6, active=True),
    PlayerXTeam(player_id=50504017, team_id=6, active=True),
    PlayerXTeam(player_id=40477718, team_id=6, active=True),
    PlayerXTeam(player_id=41431064, team_id=6, active=True),
    PlayerXTeam(player_id=36380381, team_id=6, active=True),
    PlayerXTeam(player_id=38836926, team_id=6, active=True),
    PlayerXTeam(player_id=47379755, team_id=6, active=True),
    PlayerXTeam(player_id=50045701, team_id=6, active=True),
    PlayerXTeam(player_id=48175431, team_id=6, active=True),
    PlayerXTeam(player_id=45916483, team_id=6, active=True),
    PlayerXTeam(player_id=50768656, team_id=6, active=True),
    PlayerXTeam(player_id=48695804, team_id=6, active=True),
    PlayerXTeam(player_id=47008485, team_id=6, active=True),
    PlayerXTeam(player_id=50045759, team_id=6, active=True),
    PlayerXTeam(player_id=50228826, team_id=6, active=True),


    # ======================
    # ONCE_UNIDOS (team_id=8)
    # ======================


    PlayerXTeam(player_id=36386187, team_id=8, active=True),
    PlayerXTeam(player_id=40477789, team_id=8, active=True),
    PlayerXTeam(player_id=41987218, team_id=8, active=True),
    PlayerXTeam(player_id=41987213, team_id=8, active=True),
    PlayerXTeam(player_id=36858579, team_id=8, active=True),
    PlayerXTeam(player_id=33641619, team_id=8, active=True),
    PlayerXTeam(player_id=47886816, team_id=8, active=True),
    PlayerXTeam(player_id=49341398, team_id=8, active=True),
    PlayerXTeam(player_id=45916377, team_id=8, active=True),
    PlayerXTeam(player_id=40095804, team_id=8, active=True),
    PlayerXTeam(player_id=39278358, team_id=8, active=True),
    PlayerXTeam(player_id=44267459, team_id=8, active=True),
    PlayerXTeam(player_id=45038383, team_id=8, active=True),
    PlayerXTeam(player_id=35092954, team_id=8, active=True),
    PlayerXTeam(player_id=49124390, team_id=8, active=True),
    PlayerXTeam(player_id=33159185, team_id=8, active=True),
    PlayerXTeam(player_id=49249180, team_id=8, active=True),
    PlayerXTeam(player_id=44861276, team_id=8, active=True),
    PlayerXTeam(player_id=38292625, team_id=8, active=True),


    # ======================
    #SUD_AMERICA (team_id=11)
    # ======================

    PlayerXTeam(player_id=34000856, team_id=11, active=True),
    PlayerXTeam(player_id=44861232, team_id=11, active=True),
    PlayerXTeam(player_id=43591631, team_id=11, active=True),
    PlayerXTeam(player_id=32482528, team_id=11, active=True),
    PlayerXTeam(player_id=34218185, team_id=11, active=True),
    PlayerXTeam(player_id=41717620, team_id=11, active=True),
    PlayerXTeam(player_id=36585981, team_id=11, active=True),
    PlayerXTeam(player_id=45292906, team_id=11, active=True),
    PlayerXTeam(player_id=36361844, team_id=11, active=True),
    PlayerXTeam(player_id=43591617, team_id=11, active=True),
    PlayerXTeam(player_id=50589967, team_id=11, active=True),
    PlayerXTeam(player_id=40477844, team_id=11, active=True),
    PlayerXTeam(player_id=41717578, team_id=11, active=True),
    PlayerXTeam(player_id=41068500, team_id=11, active=True),
    PlayerXTeam(player_id=34032306, team_id=11, active=True),
    PlayerXTeam(player_id=33159201, team_id=11, active=True),
    PlayerXTeam(player_id=43591613, team_id=11, active=True),
    PlayerXTeam(player_id=47379743, team_id=11, active=True),
    PlayerXTeam(player_id=44640818, team_id=11, active=True),
    PlayerXTeam(player_id=36585989, team_id=11, active=True),
    PlayerXTeam(player_id=41540901, team_id=11, active=True),
    PlayerXTeam(player_id=42573067, team_id=11, active=True),


    # ======================
    #POLVORIN (team_id=5)
    # ======================


    PlayerXTeam(player_id=44417400, team_id=5, active=True),
    PlayerXTeam(player_id=43015424, team_id=5, active=True),
    PlayerXTeam(player_id=46959135, team_id=5, active=True),
    PlayerXTeam(player_id=38352854, team_id=5, active=True),
    PlayerXTeam(player_id=36361869, team_id=5, active=True),
    PlayerXTeam(player_id=38292527, team_id=5, active=True),
    PlayerXTeam(player_id=42434282, team_id=5, active=True),
    PlayerXTeam(player_id=49252991, team_id=5, active=True),
    PlayerXTeam(player_id=42573017, team_id=5, active=True),
    PlayerXTeam(player_id=42573022, team_id=5, active=True),
    PlayerXTeam(player_id=45946355, team_id=5, active=True),
    PlayerXTeam(player_id=43015422, team_id=5, active=True),
    PlayerXTeam(player_id=41431160, team_id=5, active=True),
    PlayerXTeam(player_id=44861116, team_id=5, active=True),
    PlayerXTeam(player_id=45811141, team_id=5, active=True),
    PlayerXTeam(player_id=49252802, team_id=5, active=True),
    PlayerXTeam(player_id=45916191, team_id=5, active=True),
    PlayerXTeam(player_id=94953478, team_id=5, active=True),
    PlayerXTeam(player_id=36586193, team_id=5, active=True),
    PlayerXTeam(player_id=49115267, team_id=5, active=True),


    # ======================
    #ATLETICO_MIRAMAR (team_id=12)
    # ======================


    PlayerXTeam(player_id=47738826, team_id=12, active=True),
    PlayerXTeam(player_id=41717618, team_id=12, active=True),
    PlayerXTeam(player_id=41987271, team_id=12, active=True),
    PlayerXTeam(player_id=41987337, team_id=12, active=True),
    PlayerXTeam(player_id=40063673, team_id=12, active=True),
    PlayerXTeam(player_id=40477722, team_id=12, active=True),
    PlayerXTeam(player_id=41831528, team_id=12, active=True),
    PlayerXTeam(player_id=46631035, team_id=12, active=True),
    PlayerXTeam(player_id=33482555, team_id=12, active=True),
    PlayerXTeam(player_id=33494409, team_id=12, active=True),
    PlayerXTeam(player_id=43906803, team_id=12, active=True),
    PlayerXTeam(player_id=48592857, team_id=12, active=True),
    PlayerXTeam(player_id=30099064, team_id=12, active=True),
    PlayerXTeam(player_id=42455944, team_id=12, active=True),
    PlayerXTeam(player_id=44417438, team_id=12, active=True),
    PlayerXTeam(player_id=40095760, team_id=12, active=True),
    PlayerXTeam(player_id=44861178, team_id=12, active=True),
    PlayerXTeam(player_id=37017965, team_id=12, active=True),


    # ======================
    #HURACANES (team_id=9)
    # ======================


    PlayerXTeam(player_id=48695717, team_id=9, active=True),
    PlayerXTeam(player_id=32930364, team_id=9, active=True),
    PlayerXTeam(player_id=47886882, team_id=9, active=True),
    PlayerXTeam(player_id=35796942, team_id=9, active=True),
    PlayerXTeam(player_id=30147535, team_id=9, active=True),
    PlayerXTeam(player_id=44861084, team_id=9, active=True),
    PlayerXTeam(player_id=40477843, team_id=9, active=True),
    PlayerXTeam(player_id=40878578, team_id=9, active=True),
    PlayerXTeam(player_id=45579172, team_id=9, active=True),
    PlayerXTeam(player_id=34218218, team_id=9, active=True),
    PlayerXTeam(player_id=43893865, team_id=9, active=True),
    PlayerXTeam(player_id=48982590, team_id=9, active=True),
    PlayerXTeam(player_id=47072913, team_id=9, active=True),
    PlayerXTeam(player_id=37363603, team_id=9, active=True),
    PlayerXTeam(player_id=39278416, team_id=9, active=True),
    PlayerXTeam(player_id=28185483, team_id=9, active=True),
    PlayerXTeam(player_id=47886863, team_id=9, active=True),
    PlayerXTeam(player_id=35796766, team_id=9, active=True),
    PlayerXTeam(player_id=30568618, team_id=9, active=True),


    # ======================
    #JUVENTUD_UNIDA (team_id=2)
    # ======================


    PlayerXTeam(player_id=48089115, team_id=2, active=True),
    PlayerXTeam(player_id=40831725, team_id=2, active=True),
    PlayerXTeam(player_id=45916136, team_id=2, active=True),
    PlayerXTeam(player_id=41540803, team_id=2, active=True),
    PlayerXTeam(player_id=32985755, team_id=2, active=True),
    PlayerXTeam(player_id=45579188, team_id=2, active=True),
    PlayerXTeam(player_id=42398442, team_id=2, active=True),
    PlayerXTeam(player_id=42398488, team_id=2, active=True),
    PlayerXTeam(player_id=45397788, team_id=2, active=True),
    PlayerXTeam(player_id=40308207, team_id=2, active=True),
    PlayerXTeam(player_id=44050476, team_id=2, active=True),
    PlayerXTeam(player_id=44417405, team_id=2, active=True),
    PlayerXTeam(player_id=45579158, team_id=2, active=True),
    PlayerXTeam(player_id=40308212, team_id=2, active=True),
    PlayerXTeam(player_id=46103675, team_id=2, active=True),
    PlayerXTeam(player_id=33057173, team_id=2, active=True),
    PlayerXTeam(player_id=35342993, team_id=2, active=True),
    PlayerXTeam(player_id=40831729, team_id=2, active=True),
    PlayerXTeam(player_id=48427746, team_id=2, active=True),
    PlayerXTeam(player_id=37605240, team_id=2, active=True),


    # ======================
    #SAN_MARTIN (team_id=7)
    # ======================


    PlayerXTeam(player_id=38292596, team_id=7, active=True),
    PlayerXTeam(player_id=45296557, team_id=7, active=True),
    PlayerXTeam(player_id=46272006, team_id=7, active=True),
    PlayerXTeam(player_id=39278439, team_id=7, active=True),
    PlayerXTeam(player_id=41540988, team_id=7, active=True),
    PlayerXTeam(player_id=45296545, team_id=7, active=True),
    PlayerXTeam(player_id=38586189, team_id=7, active=True),
    PlayerXTeam(player_id=41516431, team_id=7, active=True),
    PlayerXTeam(player_id=47886880, team_id=7, active=True),
    PlayerXTeam(player_id=39830483, team_id=7, active=True),
    PlayerXTeam(player_id=41987242, team_id=7, active=True),
    PlayerXTeam(player_id=34855199, team_id=7, active=True),
    PlayerXTeam(player_id=46631015, team_id=7, active=True),
    PlayerXTeam(player_id=39287559, team_id=7, active=True),
    PlayerXTeam(player_id=47334160, team_id=7, active=True),
    PlayerXTeam(player_id=45296555, team_id=7, active=True),
    PlayerXTeam(player_id=47886888, team_id=7, active=True),
    PlayerXTeam(player_id=37017986, team_id=7, active=True),


    # ======================
    #DEFENSORES_DEL_SUR (team_id=10)
    # ======================


    PlayerXTeam(player_id=42233395, team_id=10, active=True),
    PlayerXTeam(player_id=35339953, team_id=10, active=True),
    PlayerXTeam(player_id=37869535, team_id=10, active=True),
    PlayerXTeam(player_id=32638901, team_id=10, active=True),
    PlayerXTeam(player_id=36081154, team_id=10, active=True),
    PlayerXTeam(player_id=95824850, team_id=10, active=True),
    PlayerXTeam(player_id=39102632, team_id=10, active=True),
    PlayerXTeam(player_id=33996478, team_id=10, active=True),
    PlayerXTeam(player_id=36848502, team_id=10, active=True),
    PlayerXTeam(player_id=95890085, team_id=10, active=True),
    PlayerXTeam(player_id=95721759, team_id=10, active=True),
    PlayerXTeam(player_id=41934669, team_id=10, active=True),
    PlayerXTeam(player_id=37983902, team_id=10, active=True),
    PlayerXTeam(player_id=41429063, team_id=10, active=True),
    PlayerXTeam(player_id=44619234, team_id=10, active=True),
    PlayerXTeam(player_id=34644727, team_id=10, active=True),
    PlayerXTeam(player_id=37405685, team_id=10, active=True),
    PlayerXTeam(player_id=37483402, team_id=10, active=True),
    PlayerXTeam(player_id=51336933, team_id=10, active=True),


    # ======================
    #QUILMES (team_id=4)
    # ======================


    PlayerXTeam(player_id=41431200, team_id=4, active=True),
    PlayerXTeam(player_id=41431079, team_id=4, active=True),
    PlayerXTeam(player_id=34255113, team_id=4, active=True),
    PlayerXTeam(player_id=31024514, team_id=4, active=True),
    PlayerXTeam(player_id=38292708, team_id=4, active=True),
    PlayerXTeam(player_id=42344855, team_id=4, active=True),
    PlayerXTeam(player_id=38688650, team_id=4, active=True),
    PlayerXTeam(player_id=40477800, team_id=4, active=True),
    PlayerXTeam(player_id=31828859, team_id=4, active=True),
    PlayerXTeam(player_id=37864253, team_id=4, active=True),
    PlayerXTeam(player_id=45397887, team_id=4, active=True),
    PlayerXTeam(player_id=45811192, team_id=4, active=True),
    PlayerXTeam(player_id=28185502, team_id=4, active=True),
    PlayerXTeam(player_id=35333412, team_id=4, active=True),
    PlayerXTeam(player_id=43906885, team_id=4, active=True),
    PlayerXTeam(player_id=42434242, team_id=4, active=True),
    PlayerXTeam(player_id=45397728, team_id=4, active=True),

]

db.add_all(relations)
db.commit()
db.close()

print("PlayerXTeam cargado correctamente")