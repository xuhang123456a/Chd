swopDatas = {
    70505301,
    70505302,
    70505303,
    70505304,
    70505305,
    70505306,
    70505307,
    70505308,
    70505309,
    70505310,
    70505311,
    70505312,
    70505313,
    }

    system_print("兑换圣字宝石魔法锤到圣字之火-开始")
    npc_start(88902)
    _sleep(500)
    local iSwopCount = 1
    while (iSwopCount ~= 0)do
        iSwopCount = 0
        for key, value in pairs(swopDatas) do
            index = key - 1
            if (npc_swop(88902,28813,index,100000,value,1) == 1)
            then
                system_print("兑换一件物品到圣字之火.")
                iSwopCount = 1
                break
            end
        end
        _sleep(500)
    end
    npc_end(88902)
    system_print("兑换圣字宝石魔法锤到圣字之火-结束")