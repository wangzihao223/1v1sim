from make_distribution import*


def troop_assembly(start, width, size):
    return make_uniform(start, width, size)


def networking_building(start, width, size):
    return make_uniform(start, width, size)


def detection_range(start, width, size):
    return make_uniform(start, width, size)


def target_integrity(n, p, size):
    return np.random.binomial(n, p, size=size)


def reaction_time(start, width, size):
    return make_uniform(start, width, size)


def target_recognition(miu, sigma, size, n, p):
     m = make_gaussian(miu, sigma, size)
     z = make_binomial(n, p, size)
     return ["识别距离", m ,"识别正确率",z,]

def battlefield_situation(miu, sigma, n, p, size):
    w = make_binomial(n, p, size)
    s = make_gaussian(miu, sigma, size)
    return ("完整度", w, "形成时间", s)
