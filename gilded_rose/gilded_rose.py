class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self.increase_quality(item, -1)
            else:
                max_quality = 50
                if item.quality < max_quality:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.quality < max_quality:
                        if item.sell_in < 6:
                            self.increase_quality(item, 2)
                        elif item.sell_in < 11:
                            self.increase_quality(item, 1)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                self.increase_quality(item, -1)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        self.increase_quality(item, 1)

    def increase_quality(self, item, increment):
        item.quality += increment
