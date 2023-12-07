from loguru import logger

from aoc_2023.utils import by_double_line, get_day_and_input


class Mapper:
    def __init__(self, name, mappings):
        self.name = name
        self.mappings = mappings

    def map(self, v):
        for m in self.mappings:
            mapped_v = m.map(v)
            if v != mapped_v:
                return mapped_v
        return v


class Mapping:
    def __init__(self, source, dest, mrange):
        self.source = source
        self.dest = dest
        self.range = mrange

    def map(self, v):
        if self.source <= v < self.source + self.range:
            return self.dest + v - self.source
        return v


def build_mapper(instrs):
    name, *mappings = instrs.split("\n")
    name = name.split()[0]
    m = []
    for mapping in mappings:
        dest, source, rang = [int(i) for i in mapping.split()]
        m.append(Mapping(source, dest, rang))

    return Mapper(name, m)


def parse_maps(instructions):
    seeds = [int(i) for i in instructions[0].split(":")[1].split()]
    seed_to_soil = instructions[1]
    soil_to_fert = instructions[2]
    fert_to_water = instructions[3]
    water_to_light = instructions[4]
    light_to_temp = instructions[5]
    temp_to_hum = instructions[6]
    hum_to_loc = instructions[7]

    s_s_mapper = build_mapper(seed_to_soil)
    s_f_mapper = build_mapper(soil_to_fert)
    f_w_mapper = build_mapper(fert_to_water)
    w_l_mapper = build_mapper(water_to_light)
    l_t_mapper = build_mapper(light_to_temp)
    t_h_mapper = build_mapper(temp_to_hum)
    h_l_mapper = build_mapper(hum_to_loc)

    return seeds, {
        m.name: m for m in [s_s_mapper, s_f_mapper, f_w_mapper, w_l_mapper, l_t_mapper, t_h_mapper, h_l_mapper]
    }


def get_locations(seeds, maps):
    locations = []

    for seed in seeds:
        soil = maps["seed-to-soil"].map(seed)
        fert = maps["soil-to-fertilizer"].map(soil)
        water = maps["fertilizer-to-water"].map(fert)
        light = maps["water-to-light"].map(water)
        temp = maps["light-to-temperature"].map(light)
        hum = maps["temperature-to-humidity"].map(temp)
        loc = maps["humidity-to-location"].map(hum)
        locations.append(loc)
    return locations


def part_1(data):
    map_instructions = by_double_line(data)
    seeds, maps = parse_maps(map_instructions)

    locations = get_locations(seeds, maps)

    return min(locations)


def part_2(data):
    map_instructions = by_double_line(data)
    seeds, maps = parse_maps(map_instructions)
    for k, mapper in maps.items():
        for mapping in mapper.mappings:
            mapping.source, mapping.dest = mapping.dest, mapping.source

    min_seed = min(seeds[::2])
    for loc in range(10000000000):
        hum = maps["humidity-to-location"].map(loc)
        temp = maps["temperature-to-humidity"].map(hum)
        light = maps["light-to-temperature"].map(temp)
        water = maps["water-to-light"].map(light)
        fert = maps["fertilizer-to-water"].map(water)
        soil = maps["soil-to-fertilizer"].map(fert)

        seed = maps["seed-to-soil"].map(soil)

        if seed < min_seed:
            continue
        for start, srange in zip(seeds[::2], seeds[1::2]):
            if start <= seed < start + srange:
                return loc
        if loc % 1000000 == 0:
            logger.debug(loc)


def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


def test_part_1():
    s = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    assert part_1(s) == 35


def test_part_2():
    s = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    assert part_2(s) == 46
