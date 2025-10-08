# 🧙 Defeat the Evil Wizard

A turn-based RPG battle game where you choose a character class and fight against an evil wizard. Built with Python using object-oriented programming principles.

## 🎮 How to Play

Run the game:
```bash
python DefeatTheWiz.py
```

Choose from 4 character classes, each with unique abilities:
- **Warrior** ⚔️ - High health tank with rage-based abilities
- **Mage** 🔥 - Glass cannon with powerful spells and mana management
- **Archer** 🏹 - Precision fighter with crowd control
- **Paladin** 🛡️ - Holy warrior with healing and defense

## 🔧 Technical Implementation

### Object-Oriented Design
I structured the game using inheritance - all character classes extend a base `Character` class. This let me share common functionality (attack, heal, stats) while allowing each class to override methods for unique behaviors.

### Resource Management Systems
Each class has its own resource mechanic:
- Warriors build **rage** through attacks
- Mages regenerate **mana** each turn
- Archers gain **focus** over time
- Paladins accumulate **holy power**

These resources are spent on special abilities, adding strategic depth.

### Polymorphism in Action
The `use_special_ability()` method is defined in the base class but implemented differently for each character. Same interface, different behaviors - classic polymorphism.

### Random Damage Ranges
Attacks deal random damage within a range (50-150% of base attack power) using Python's `random` module. This adds variability and prevents battles from being too predictable.

### Status Effects & Turn Tracking
I implemented a turn counter system for the wizard's special ability and a stun mechanic that affects turn flow. The `is_stunned` flag demonstrates how to manage state across turns.

### Special Method Overriding
Classes like Warrior and Paladin override `take_damage()` to implement defensive abilities (Shield Wall, Divine Shield) that modify incoming damage calculations.

## 🎯 Game Features

- 4 playable classes with unique playstyles
- Special abilities with resource costs
- Healing potion system (3 potions per battle)
- Boss with regeneration and special attacks
- Random damage for dynamic combat

## 🧠 What I Learned

This project helped me practice:
- Class inheritance and method overriding
- Managing object state across turns
- Implementing game loops and turn-based logic
- Using `isinstance()` for type checking
- Building interactive CLI menus

The code demonstrates how OOP principles make it easy to extend the game - adding a new character class just requires creating a new subclass and implementing its abilities.