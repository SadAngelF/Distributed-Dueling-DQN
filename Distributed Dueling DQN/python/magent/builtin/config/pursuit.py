import magent


def get_config(map_size):
    gw = magent.gridworld
    cfg = gw.Config()

    cfg.set({"map_width": map_size, "map_height": map_size})

    predator1 = cfg.register_agent_type(
        "predator1",
        {
            'width': 2, 'length': 2, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2
        })

    cfg.set({"map_width": map_size, "map_height": map_size})

    predator2 = cfg.register_agent_type(
        "predator2",
        {
            'width': 2, 'length': 2, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2
        })

    cfg.set({"map_width": map_size, "map_height": map_size})

    predator3 = cfg.register_agent_type(
        "predator3",
        {
            'width': 2, 'length': 2, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2
        })

    cfg.set({"map_width": map_size, "map_height": map_size})

    predator4 = cfg.register_agent_type(
        "predator4",
        {
            'width': 2, 'length': 2, 'hp': 1, 'speed': 1,
            'view_range': gw.CircleRange(5), 'attack_range': gw.CircleRange(2),
            'attack_penalty': -0.2
        })

    prey = cfg.register_agent_type(
        "prey",
        {
            'width': 1, 'length': 1, 'hp': 1, 'speed': 1.5,
            'view_range': gw.CircleRange(4), 'attack_range': gw.CircleRange(0)
        })

    predator_group1  = cfg.add_group(predator1)
    predator_group2  = cfg.add_group(predator2)
    predator_group3  = cfg.add_group(predator3)
    predator_group4  = cfg.add_group(predator4)
    prey_group = cfg.add_group(prey)

    a = gw.AgentSymbol(predator_group1, index='any')
    b = gw.AgentSymbol(predator_group2, index='any')
    c = gw.AgentSymbol(predator_group3, index='any')
    d = gw.AgentSymbol(predator_group4, index='any')
    e = gw.AgentSymbol(prey_group, index='any')

    e1 = gw.Event(a, 'attack', e)
    e2 = gw.Event(b, 'attack', e)
    e3 = gw.Event(c, 'attack', e)
    e4 = gw.Event(d, 'attack', e)


    cfg.add_reward_rule(e1 , receiver=[a, e], value=[1, -1])
    cfg.add_reward_rule(e2 , receiver=[b, e], value=[1, -1])
    cfg.add_reward_rule(e3 , receiver=[c, e], value=[1, -1])
    cfg.add_reward_rule(e4 , receiver=[d, e], value=[1, -1])
    cfg.add_reward_rule(e1 & e2 , receiver=[a, b, e], value=[1, 1, -1])
    cfg.add_reward_rule(e1 & e3 , receiver=[a, c, e], value=[1, 1, -1])
    cfg.add_reward_rule(e1 & e4 , receiver=[a, d, e], value=[1, 1, -1])
    cfg.add_reward_rule(e2 & e3 , receiver=[c, b, e], value=[1, 1, -1])
    cfg.add_reward_rule(e3 & e4 , receiver=[c, d, e], value=[1, 1, -1])
    cfg.add_reward_rule(e4 & e2 , receiver=[d, b, e], value=[1, 1, -1])
    cfg.add_reward_rule(e1 & e2 & e3 , receiver=[a, b, c, e], value=[1, 1, 1, -1])
    cfg.add_reward_rule(e1 & e2 & e4 , receiver=[a, b, d, e], value=[1, 1, 1, -1])
    cfg.add_reward_rule(e1 & e4 & e3 , receiver=[a, d, c, e], value=[1, 1, 1, -1])
    cfg.add_reward_rule(e4 & e2 & e3 , receiver=[d, b, c, e], value=[1, 1, 1, -1])
    cfg.add_reward_rule(e1 & e2 & e3 &e4, receiver=[a, b, c, d,e], value=[1, 1, 1, 1,-1])


    return cfg
