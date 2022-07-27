import mesa

# agente do modelo
class SchellingAgent(mesa.Agent):

    # cria um agente
    # agent_type = 0 (minoritario) ou 1 (majoritario)
    def __init__(self, pos, model, agent_type):
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type

    def step(self):
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1

        # move se nao estiver feliz
        if similar < self.model.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1

# modelo de segregacao
class Schelling(mesa.Model):

    # largura = 20
    # altura = 20
    # densidade = 0.8 (densidade de agentes no sistema)
    # fracao_minoritario = 0.2 (fracao de agentes minoritarios)
    # homophily = 3 (quantidade de agentes que devem ser similares para que outro agente seja feliz)
    def __init__(self, width=20, height=20, density=0.8, minority_pc=0.2, homophily=3):
        self.width = width
        self.height = height
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        self.happy = 0
        self.datacollector = mesa.DataCollector({"happy": "happy"},{"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]},)

        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                if self.random.random() < self.minority_pc:
                    agent_type = 1
                else:
                    agent_type = 0

                agent = SchellingAgent((x, y), self, agent_type)
                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.happy = 0
        self.schedule.step()
        self.datacollector.collect(self)

        if self.happy == self.schedule.get_agent_count():
            self.running = False