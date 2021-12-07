class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            sulfuras = "Sulfuras, Hand of Ragnaros"
            backstage_passes = "Backstage passes to a TAFKAL80ETC concert"
            brie = "Aged Brie"

            if item.name == sulfuras:
                continue
            
            if item.name != brie and item.name != backstage_passes:
                self.increase_quality(item, -1)

            else:
                self.increase_quality(item, 1)

                if item.name == backstage_passes:
                    if item.sell_in < 6:
                        self.increase_quality(item, 2)

                    elif item.sell_in < 11:
                        self.increase_quality(item, 1)

            item.sell_in -= 1
            
            if item.sell_in < 0:
                
                if item.name == brie:                    
                    self.increase_quality(item, 1)                    
                else:
                    if item.name == backstage_passes:
                        item.quality -= item.quality                        
                    else:
                        self.increase_quality(item, -1)

    def increase_quality(self, item, increment):
        max_quality = 50
        if item.quality < max_quality:
            item.quality += increment
        
        if item.quality > max_quality:
            item.quality = max_quality

        if item.quality < 0:
            item.quality = 0
