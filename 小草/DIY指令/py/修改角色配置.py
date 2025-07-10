import os
import json
from src.utils.tools import read_json_file, save_json_file, modify_json_data

target_path = r'E:\Game\Chd\小草\心月狐\data\Config'
target_files_path = [
    ["﹎秋水伊人ゞ", "1536622268\\A96DC7EFCBAED2C1C8CBA967"],
    ["晚来天欲雪o", "1536622268\\CDEDC0B4CCECD3FBD1A96F"],
    # ["小姐姐", "1536622268\\D7FAD7FAD7FAD7FAD7FAD0A1BDE3BDE3"],
    # ["云青青兮欲雨", "1536622268\\D4C6C7E0C7E0D9E2D3FBD3EAFE5D"],
    ["满船清梦压星河Q", "1536622268\\C2FAB4ACC7E5C3CED1B9D0C7BAD351"],
    # ["能饮一杯无o", "1536622268\\C4DCD2FBD2BBB1ADCEDE6F"],
    # ["醉后不知天在水o", "1536622268\\D7EDBAF3B2BBD6AACCECD4DACBAE6F"],
    # ["→酷我音乐→", "1536622268\\A1FABFE1CED2D2F4C0D6A1FA"],
    # ["酷狗音乐ā", "1536622268\\BFE1B9B7D2F4C0D6A8A1"],
    # ["℃ベ裸装", "1536622268\\A1E6A5D9A8FDA8FDC2E3D7B0"],
    # ["终不似o", '1536622268\\D6D5B2BBCBC66F'],
    # ["最是人间留不住o", "1536622268\\D7EECAC7C8CBBCE4C1F4B2BBD7A16F"],
    # ["水澹澹兮生烟", "1536622268\\CBAEE5A3E5A3D9E2C9FAD1CCFE5D"],
    # ["少年游o", "1536622268\\C9D9C4EAD3CE6F"],

    # ["你到底吻不吻我o", "3387891881\\C4E3B5BDB5D7CEC7B2BBCEC7CED26F"],
    # ["来去荒芜", "3387891881\\C0B4C8A5BBC4CEDF"],
    # ["不要碰我肩膀", "3387891881\\B2BBD2AAC5F6CED2BCE7B0F2"],
    # ["逾白","3387891881\\D3E2B0D7FE5D"],
    # ["陌辰","3387891881\\C4B0B3BD"],
    # ["我有药", "3387891881\\CED2D3D0D2A9"],
    # ["惊觉","3387891881\\BEAABEF5FE5D"],
    # ["乙骨犹太","3387891881\\D2D2B9C7D3CCCCAB"],
    # ["心缩","3387891881\\D0C4CBF5"],
    # ["鸦九","3387891881\\D1BBBEC5"],
    # ["烟雨情相思","3387891881\\D7FAD1CCD3EAC7E9CFE0CBBCD7FA"],
    # ["荼茶","3387891881\\DDB1B2E8"],
    # ["莫吵","3387891881\\C4AAB3B3"],
    # ["无心梦","3387891881\\CEDED0C4C3CE"],

    # ["自然萌ご", "3476670590\\D7FCD7FCD7D4C8BBC3C8A4B4D7FC"],
    # ["十八岁青春男高", "3476670590\\CAAEB0CBCBEAC7E0B4BAC4D0B8DF"],
    # ["雪绒薄荷ご", "3476670590\\D7FCD7FCD1A9C8DEB1A1BAC9A4B4"],
    # ["傻海我们走~", "3476670590\\C9B5BAA3CED2C3C7D7DF7E"],
    # ["BaLl,", "3476670590\\42614C6C2C"],
    # ["萌萌仓库-格挡","3476670590\\C3C8C3C8B2D6BFE22DB8F1B5B2"],
    # ["萌萌仓库-爆率","3476670590\\C3C8C3C8B2D6BFE22DB1ACC2CA"],
    # ["芝士羊绒ご","3476670590\\D7FCD7FCD6A5CABFD1F2C8DEA4B4"],
    # ["雪绒蓝莓ご","3476670590\\D7FCD7FCD1A9C8DEC0B6DDAEA4B4"],
]
for target_file_path in target_files_path:
    target_file_path = os.path.join(target_path, target_file_path[1])
    target_file_path = os.path.join(target_file_path, 'Default.save')
    target_json_content = read_json_file(target_file_path)
    # 修改 JSON 数据
    key = "diytrigger"
    new_value = [{
			"only_run":	False,
			"run_sleep":	0,
			"sw":	True,
			"name":	"超越点切换",
			"judges":	[{
					"sw":	False,
					"judge":	{
						"在副本频道":	""
					}
				}],
			"executes":	[{
					"sw":	False,
					"sleep":	"0",
					"execute":	{
						"超越搭配":	"异常状态防御"
					},
					"judges":	[{
							"中异常状态":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"超越搭配":	"小怪属性"
					},
					"judges":	[{
							"地图内无首领":	""
						}, {
							"未中异常状态":	""
						}, {
							"地图内无怪":	"重力引流员;"
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"超越搭配":	"BOSS属性"
					},
					"judges":	[{
							"地图内有首领":	""
						}, {
							"未中异常状态":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"超越搭配":	"BOSS属性"
					},
					"judges":	[{
							"地图内有怪":	"重力引流员;"
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"奈落吃药",
			"judges":	[{
					"sw":	True,
					"judge":	{
						"在副本":	"奈落·冰封雪域;奈落·破坏之城;奈落·冰淇淋庭院;奈落·珊瑚之歌;奈落·蛇龙之巢;奈落·神树拉菲尔;奈落·魔法学院主楼;"
					}
				}],
			"executes":	[{
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的魔能合剂"
					},
					"judges":	[{
							"没有BUFF":	"速效药剂:进攻型_9487019"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·秩序"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"哈密瓜味全糖蜜果"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·坚固"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"紫葡萄味全糖蜜果"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"青苹果味全糖蜜果"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·壁垒"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"优先技能":	"[奈落]聚能冲击"
					},
					"judges":	[{
							"搜索内有怪":	""
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"世界BOSS",
			"judges":	[{
					"sw":	True,
					"judge":	{
						"在地图":	"阿瓦伦 未知之处_100703;"
					}
				}, {
					"sw":	True,
					"judge":	{
						"地图内有首领":	""
					}
				}],
			"executes":	[{
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"状态物品":	"青苹果味全糖蜜果"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"【生存本能】1段"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"更换称号":	"魔尊领域掌握者"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"超越搭配":	"BOSS属性"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"智者超载之钥"
					},
					"judges":	[{
							"首领HP百分比<=":	"50"
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]神之使者"
					},
					"judges":	[]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"装备切换",
			"judges":	[{
					"sw":	False,
					"judge":	{
						"在副本":	"珊瑚之歌;泡泡战舰;火山超能场;珊瑚森林;"
					}
				}],
			"executes":	[{
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"切换副武器":	""
					},
					"judges":	[{
							"在地图":	"珊瑚森林 2_30401;努特的炼金猎场_89901;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"切换主武器":	""
					},
					"judges":	[{
							"在地图":	"珊瑚森林 3_30402;艾丽娅斯城市_600;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"强力戒指(12小时)"
					},
					"judges":	[{
							"在副本":	"珊瑚之歌;泡泡战舰;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"强力戒指(3小时)"
					},
					"judges":	[{
							"在副本":	"珊瑚之歌;泡泡战舰;"
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"困难庭院",
			"judges":	[{
					"sw":	True,
					"judge":	{
						"在副本":	"阿特拉斯庭院;"
					}
				}, {
					"sw":	True,
					"judge":	{
						"在困难副本":	""
					}
				}],
			"executes":	[{
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·秩序"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·远古"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·暴怒"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·壁垒"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"青苹果味全糖蜜果"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"紫葡萄味全糖蜜果"
					},
					"judges":	[{
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"优先技能":	"【生存本能】1段"
					},
					"judges":	[{
							"不在地图":	"阿特拉斯庭院 8_106108;阿特拉斯庭院 7_106107;阿特拉斯庭院 6_106106;阿特拉斯庭院 5_106105;阿特拉斯庭院 4_106104;阿特拉斯庭院 3_106103;阿特拉斯庭院 2_106102;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"优先技能":	"【生存本能】2段"
					},
					"judges":	[{
							"在地图":	"阿特拉斯庭院 8_106108"
						}, {
							"首领血条数<=":	"90"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的铁盾药剂"
					},
					"judges":	[{
							"没有BUFF":	"家族·冰魔图腾_63020219"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"哈密瓜味全糖蜜果"
					},
					"judges":	[{
							"没有BUFF":	"家族·冰魔图腾_63020219"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉兰大道的晚餐·过去的真理"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"装模作样绿茶姐"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉兰大道的晚餐·过去的真理"
					},
					"judges":	[{
							"在地图":	"阿特拉斯庭院 5_106105;阿特拉斯庭院 6_106106;阿特拉斯庭院 7_106107;阿特拉斯庭院 8_106108;阿特拉斯庭院 3_106103;阿特拉斯庭院 4_106104;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"守护领域掌握者"
					},
					"judges":	[{
							"在地图":	"阿特拉斯庭院 1_106101;阿特拉斯庭院 2_106102;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"装模作样绿茶姐"
					},
					"judges":	[{
							"在地图":	"阿特拉斯庭院 3_106103;阿特拉斯庭院 4_106104;阿特拉斯庭院 5_106105;阿特拉斯庭院 6_106106;阿特拉斯庭院 7_106107;阿特拉斯庭院 8_106108;"
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"称号切换有守护",
			"judges":	[],
			"executes":	[{
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"守护领域掌握者"
					},
					"judges":	[{
							"在副本":	"精灵树桩;奈落·冰封雪域;奈落·破坏之城;奈落·冰淇淋庭院;奈落·珊瑚之歌;奈落·蛇龙之巢;流水回廊;艾乌加蒙剧场;深渊之镜;未知森林;穿梭之都;无尽繁星大厅;大地的考验;黄昏教堂;生命之恩泰莱凯;埃吉尔遗迹;群星宫殿;奈落·神树拉菲尔;奈落·魔法学院主楼;时空之泉;穆斯菲尔斯隧道;尼夫海姆站;诺尼尔之泪;摩克沙;薇娅斯梦境;水下培养皿·失魂寺;丽西泰亚之门;蘑菇树沼泽;普累罗麻;残缺边界;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"巧克力甜品大师"
					},
					"judges":	[{
							"在地图":	"塞丽娜城_63400;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"为了卡兹诺的幸福"
					},
					"judges":	[{
							"在地图":	"星之仓库_21002;古木丛林入口_4700;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"救梦者"
					},
					"judges":	[{
							"在副本":	"普累罗麻;残缺边界;"
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	False,
			"name":	"切胸针",
			"judges":	[],
			"executes":	[{
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"扬卡什胸针+4"
					},
					"judges":	[{
							"拥有BUFF":	"充能_88232992"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"利卡里亚之双生胸针"
					},
					"judges":	[{
							"拥有BUFF":	"充能_88230050"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"利卡里亚之双生胸针"
					},
					"judges":	[{
							"没有BUFF":	"充能_88220050"
						}, {
							"没有BUFF":	"充能_88232992"
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"无守护普通本吃药",
			"judges":	[{
					"sw":	True,
					"judge":	{
						"在副本频道":	""
					}
				}],
			"executes":	[{
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·壁垒"
					},
					"judges":	[{
							"在地图":	"阿特拉斯庭院 6_106106;阿特拉斯庭院 8_106108;阿特拉斯庭院 1_106101;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·壁垒"
					},
					"judges":	[{
							"在副本":	"普累罗麻;"
						}, {
							"没有BUFF":	"家族·冰魔图腾_63020018"
						}, {
							"地图内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·壁垒"
					},
					"judges":	[{
							"在副本":	"残缺边界;"
						}, {
							"没有BUFF":	"家族·冰魔图腾_63020018"
						}, {
							"地图内有首领":	""
						}, {
							"在困难副本":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的铁盾药剂"
					},
					"judges":	[{
							"在地图":	"埃吉尔遗迹 6_106206;阿特拉斯庭院 6_106106;穆斯菲尔斯隧道8_107907;尼夫海姆站6_108006;阿特拉斯庭院 5_106105;阿特拉斯庭院 1_106101;精灵树桩 6_103206;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的铁盾药剂"
					},
					"judges":	[{
							"在副本":	"时空之泉;埃吉尔遗迹;诺尼尔之泪;摩克沙;穆斯菲尔斯隧道;尼夫海姆站;群星宫殿;丽西泰亚之门;蘑菇树沼泽;"
						}, {
							"没有BUFF":	"家族·冰魔图腾_63020219"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"哈密瓜味全糖蜜果"
					},
					"judges":	[{
							"在地图":	"埃吉尔遗迹 6_106206;阿特拉斯庭院 6_106106;穆斯菲尔斯隧道8_107907;尼夫海姆站6_108006;阿特拉斯庭院 5_106105;阿特拉斯庭院 1_106101;精灵树桩 6_103206;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"哈密瓜味全糖蜜果"
					},
					"judges":	[{
							"在副本":	"时空之泉;埃吉尔遗迹;诺尼尔之泪;摩克沙;穆斯菲尔斯隧道;尼夫海姆站;群星宫殿;丽西泰亚之门;蘑菇树沼泽;普累罗麻;残缺边界;"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"紫葡萄味全糖蜜果"
					},
					"judges":	[{
							"在地图":	"普累罗麻10_110110;普累罗麻6_110106;残缺边界6_110006;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"紫葡萄味全糖蜜果"
					},
					"judges":	[{
							"在副本":	"埃吉尔遗迹;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"小型伤害吸收红剂"
					},
					"judges":	[{
							"在副本":	"珊瑚之歌;阿特拉斯庭院;埃吉尔遗迹;穿梭之都;时空之泉;无尽繁星大厅;大地的考验;黑月的考验;黄昏教堂;消失的星之歌;泡泡战舰;克洛诺斯的时间;心脏的记忆;龙猫妹妹庭院;魔法学院主楼;精灵树桩;生命之恩泰莱凯;流水回廊;艾乌加蒙剧场;深渊之镜;普洛菲司台;霍普占卜室;未知森林;卡伊洛斯的时间;炼狱阿兹雷尔;巴尼塔斯;哈姆克公爵府;阿科洛之棺;圣字教堂;玫瑰庭院;卡夫卡剧场;水下培养皿·失魂寺;穆斯菲尔斯隧道;尼夫海姆站;群星宫殿;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"青苹果味全糖蜜果"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"青苹果味全糖蜜果"
					},
					"judges":	[{
							"在副本":	"普累罗麻;残缺边界;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"蓝草莓味全糖蜜果"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"蓝草莓味全糖蜜果"
					},
					"judges":	[{
							"在副本":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"甜蜜橙味全糖蜜果"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"甜蜜橙味全糖蜜果"
					},
					"judges":	[{
							"在副本":	"埃吉尔遗迹;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"红樱桃味全糖蜜果"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"红樱桃味全糖蜜果"
					},
					"judges":	[{
							"在副本":	"埃吉尔遗迹;"
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的魔能合剂"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的魔能合剂"
					},
					"judges":	[{
							"在副本":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的巨力合剂"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的巨力合剂"
					},
					"judges":	[{
							"在副本":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的稳定合剂"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的稳定合剂"
					},
					"judges":	[{
							"在副本":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的狂暴合剂"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"拉皮德的狂暴合剂"
					},
					"judges":	[{
							"在副本":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"深渊·重力药水"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"深渊·重力药水"
					},
					"judges":	[{
							"在副本":	"埃吉尔遗迹;尼夫海姆站;"
						}, {
							"搜索内有首领":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"甜蜜的突变攻击力提升药水"
					},
					"judges":	[{
							"在地图":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"甜蜜的突变攻击力提升药水"
					},
					"judges":	[{
							"在副本":	""
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"圣物生存钥匙特殊",
			"judges":	[],
			"executes":	[{
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"宏指令":	"/使用技能 圣物技能"
					},
					"judges":	[{
							"没有BUFF":	"龙猫坐像_13016169"
						}, {
							"没有BUFF":	"灼风之息_13016170"
						}, {
							"没有BUFF":	"狐狸珠_13016177"
						}, {
							"没有BUFF":	"玛阿特之眼_13016167"
						}, {
							"没有BUFF":	"圣物之力_81090001"
						}, {
							"搜索内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"宏指令":	"/使用技能 圣物技能"
					},
					"judges":	[{
							"没有BUFF":	"龙猫坐像_13016169"
						}, {
							"没有BUFF":	"灼风之息_13016170"
						}, {
							"没有BUFF":	"狐狸珠_13016177"
						}, {
							"没有BUFF":	"玛阿特之眼_13016167"
						}, {
							"没有BUFF":	"圣物之力_81090001"
						}, {
							"怪物数量>=":	"7"
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"【生存本能】1段"
					},
					"judges":	[{
							"在副本":	"奈落·冰封雪域;奈落·破坏之城;奈落·冰淇淋庭院;奈落·珊瑚之歌;奈落·蛇龙之巢;"
						}, {
							"搜索内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"【生存本能】1段"
					},
					"judges":	[{
							"不在副本":	"奈落·冰封雪域;奈落·破坏之城;奈落·冰淇淋庭院;奈落·珊瑚之歌;奈落·蛇龙之巢;阿特拉斯庭院;"
						}, {
							"在副本频道":	""
						}]
				}, {
					"sw":	False,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"【生存本能】2段"
					},
					"judges":	[{
							"在副本":	"奈落·神树拉菲尔;奈落·魔法学院主楼;奈落·冰封雪域;奈落·破坏之城;奈落·冰淇淋庭院;奈落·珊瑚之歌;奈落·蛇龙之巢;"
						}, {
							"搜索内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"智者超载之钥"
					},
					"judges":	[{
							"怪物数量>=":	"10"
						}, {
							"在副本":	"穆斯菲尔斯隧道;尼夫海姆站;群星宫殿;水下培养皿·失魂寺;阿特拉斯庭院;埃吉尔遗迹;穿梭之都;时空之泉;流水回廊;未知森林;奈落·神树拉菲尔;奈落·蛇龙之巢;奈落·珊瑚之歌;奈落·冰淇淋庭院;奈落·破坏之城;奈落·冰封雪域;奈落·魔法学院主楼;普累罗麻;残缺边界;"
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"智者超载之钥"
					},
					"judges":	[{
							"搜索内有首领":	""
						}, {
							"不在副本":	"奈落·神树拉菲尔;奈落·魔法学院主楼;奈落·冰封雪域;奈落·破坏之城;奈落·冰淇淋庭院;奈落·蛇龙之巢;"
						}, {
							"不在地图":	"阿瓦伦 未知之处_100703;尼夫海姆站1_108001;"
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"坚盾惩戒之钥"
					},
					"judges":	[{
							"搜索内有怪":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"坚盾惩戒之钥"
					},
					"judges":	[{
							"搜索内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"无畏勇者之钥"
					},
					"judges":	[{
							"搜索内有怪":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"无畏勇者之钥"
					},
					"judges":	[{
							"搜索内有首领":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]守护天使"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]梦魇恶魔"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]傀儡宗师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]英雄_双手剑"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]剑圣"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]星芒骑士_单手剑"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]武道宗师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]元素之灵"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]巨星"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]风行刺客_短剑"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]魔射手"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]远古机甲师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]通灵领主"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]英雄_枪"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]星芒骑士_钝器"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]元素之灵_风"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]风行刺客_弓箭"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]元素之灵_火"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]风行刺客_十字弓"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]天穹卡牌师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]史诗卡牌师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]黑影"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]神之使者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]阿格尼"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]逐暗者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]暗影行者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]圣十字军"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]剑刃舞者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]恐怖骑士"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]修行武者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]幻灵师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]演奏大师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]刺杀者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]审判官"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]星能机师"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]宝石星"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]疾风舞者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]唤雨之灵"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]次元守望者"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"0",
					"execute":	{
						"使用技能":	"[特殊]辉耀剑神"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用技能":	"第六感"
					},
					"judges":	[{
							"在副本频道":	""
						}]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"自动使用杂物",
			"judges":	[{
					"sw":	True,
					"judge":	{
						"不在地图":	"贝罗斯城市_200;奈落城_40200;"
					}
				}, {
					"sw":	True,
					"judge":	{
						"不在副本":	"珊瑚之歌;泡泡战舰;"
					}
				}],
			"executes":	[{
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"全塘蜜果礼盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【无限梦境】20层通关奖励"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【无限梦境II】10层通关奖励"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【无限梦境II】15层通关奖励"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【无限梦境III】4层通关奖励"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【无限梦境III】5层通关奖励"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"人品能量剂福袋"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"黄昏教堂图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"消失的星之歌图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"精灵树桩图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"生命之恩泰莱凯图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"艾乌加蒙剧场图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"深渊之镜图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"普洛菲司台图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"霍普占卜室图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"卡伊洛斯的时间图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"炼狱阿兹雷尔图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"巴尼塔斯图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"哈姆克公爵府图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"圣字教堂图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"阿科洛之棺图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"回声泉图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"冰狱图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"盟约圣地图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"希列图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"玫瑰庭院图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"幻之摇篮图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"忘却湖畔图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"虚无之星图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"山海归墟图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"梦境奥涅伊鲁图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"魔力防空洞图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"神笔画卷图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"泡泡战舰图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"克洛诺斯的时间图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"心脏的记忆图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"龙猫妹妹庭院图鉴集"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"遗忘之城怪物图鉴包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"长苔藓的箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"长苔藓的血脉箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"血脉木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"长苔藓的混沌箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"混沌木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"长苔藓的神秘箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"神秘木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"长苔藓的时间箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"时间木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·长苔藓的箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·长苔藓的血脉箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·血脉木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·长苔藓的混沌箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·混沌木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·长苔藓的神秘箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·神秘木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·长苔藓的时间箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"觉醒·时间木箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"黄金箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"黄金血脉箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"每周挑战礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"低级职业徽章包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】8层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】9层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】10层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】11层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】12层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】13层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】14层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】15层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】16层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】17层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】18层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】19层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】20层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"【奈落】20-25层护身宝石通关礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"匠人的超能装备券"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"平凡的超能装备券"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"燃炼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"清凉八月礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"耀眼的姜太公箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"闪亮的钓鱼箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"破旧的钓鱼箱子"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"中型经验药水"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"小型经验药水"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"石之塔宝箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]棕熊碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]菲轮塔碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]浑沌碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]木偶碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]粉团子碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]龙猫妹妹碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]爱丽丝碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]雷比碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]幼年独角兽碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]狐狸队长碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]粉色电气石碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]火箭龙猫碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]红龙碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]上忍碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]小山羊碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]玄武碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]丑八怪大王碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]绿企鹅碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]滑板龙猫碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]初月碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]石碑碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]传送门碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]坎贝尔碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]虎狼寺碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]上京城碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"[梦灵]回音雪地碎片"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"梦源探索包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"梦灵碎片包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"荣誉徽章I"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"荣誉徽章II"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"荣誉徽章III"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"钓鱼高手称号书"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"钓鱼达人称号书"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"钓鱼王称号书"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"钓鱼之神称号书"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"虚实宝箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"虚实宝箱 · 上品"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"史诗探险家神殿阶段礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"史诗级探险家经验药水"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"龙晶拼图卷轴宝箱"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"新年红包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"蛇年卡片盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"软噗噗的招魂盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"每日超越礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"幸运小福袋"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"变异泰伊姆斯31-40名礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"变异泰伊姆斯41-50名礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"蛇影噗噗的招魂盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"蛇影噗噗的通灵卷轴"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"龙猫舟礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"龙猫舟招魂盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"铁锤的招魂盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"冶炼礼包"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"风精灵王的心意"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"风精灵王的礼物"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"风精灵王的豪礼"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"风精灵王的馈赠"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"努特的招魂盒"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"超越图鉴包★"
					},
					"judges":	[]
				}]
		}, {
			"only_run":	False,
			"run_sleep":	1,
			"sw":	True,
			"name":	"经验本吃药",
			"judges":	[{
					"sw":	True,
					"judge":	{
						"在副本":	"珊瑚之歌;泡泡战舰;"
					}
				}],
			"executes":	[{
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"小四的祝福(不可交易)"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"百分考卷"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"经验值的秘药 500%(不可交易)"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"回忆の沙漏"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"高级温泉蛋"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"温泉蛋"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"古籍·印记"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"羁绊之羽"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"经验值药丸"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"恶魔の小果实（电）"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"恶魔の小果实（火）"
					},
					"judges":	[]
				}, {
					"sw":	False,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"恶魔の小果实（雾）"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"鳗鱼料理"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"鲤鱼料理"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"甜味饮料"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"辣鱼汤"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"短效150%经验丹(12小时)"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"领取课程戒指":	""
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"强力戒指(3小时)"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换装备":	"强力戒指(12小时)"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"状态物品":	"水蜜桃味全糖蜜果"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"更换称号":	"装模作样绿茶姐"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用技能":	"成长魔法"
					},
					"judges":	[]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"百分考卷"
					},
					"judges":	[{
							"拥有BUFF":	"活动_6000157"
						}]
				}, {
					"sw":	True,
					"sleep":	"1",
					"execute":	{
						"使用物品":	"小四的祝福(不可交易)"
					},
					"judges":	[{
							"拥有BUFF":	"活动_6000157"
						}]
				}]
		}]
    modified_json = modify_json_data(target_json_content, key, new_value)
    if modified_json:
        # 保存修改后的 JSON 文件
        save_json_file(target_file_path, modified_json, 'gbk')