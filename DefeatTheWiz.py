# Base character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def use_special_ability(self, opponent):
        """Placeholder for special abilities in subclasses."""
        pass

# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.rage_stacks = 0
        self.shield_active = False
        self.max_rage = 5

    def attack(self, opponent):
        """Warrior builds rage with each attack."""
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

        # Increase rage stacks
        if self.rage_stacks < self.max_rage:
            self.rage_stacks += 1
            print(f"⚡{self.name} gains 1 rage! Current rage: {self.rage_stacks}/{self.max_rage}")
        else:
            print(f"⚡{self.name}'s rage is at maximum!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def use_special_ability(self, opponent):
        """Display special ability menu for Warrior"""
        print("\n=== Warrior Special Abilities ===")
        print(f"Current Rage: ⚡{self.rage_stacks}/{self.max_rage}")
        print("1. Rage Strike - Deal massive damage (Costs 3 rage)")
        print("2. Shield Wall - Reduce incoming damage by 50% for 2 turns")
        print("3. Cancel")

        choice = input("Choose an ability: ")
        if choice == '1':
            return self.rage_strike(opponent)
        elif choice == '2':
            return self.shield_wall()
        elif choice == '3':
            print("Cancelled special ability.")
            return False
        else:
            print("Invalid choice. Try again.")
            return self.use_special_ability(opponent)

    def rage_strike(self, opponent):
        """Consume rage stacks to deal extra damage"""
        rage_cost = 3

        if self.rage_stacks < rage_cost:
            print(f"❌Not enough rage! Need {rage_cost}, have {self.rage_stacks}")
            print("Use regular attacks to build more rage.")
            return False

        # Consume rage and deal amplified damage
        self.rage_stacks -= rage_cost
        damage = int(self.attack_power * 2.5)
        opponent.health -= damage

        print(f"⚔️💥{self.name} uses RAGE STRIKE!")
        print(f"{self.name} unleashes fury dealing {damage} devastating damage to {opponent.name}!")
        print(f"Rage remaining: {self.rage_stacks}/{self.max_rage}")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        return True

    def shield_wall(self):
        """Activate Shield Wall to reduce incoming damage"""
        if self.shield_active:
            print("🛡️Shield Wall is already active!")
            return False

        self.shield_active = True
        print(f"🛡️{self.name} uses SHIELD WALL!")
        print(f"{self.name} will take 50% less damage for the next 2 turns!")
        return True

    def take_damage(self, damage):
        """Custom damage calculation considering Shield Wall"""
        if self.shield_active:
            damage = int(damage * 0.5)
            print(f"🛡️Shield Wall active! Damage reduced to {damage}!")
            self.shield_active = False  # Shield Wall lasts for one attack
        self.health -= damage
        return damage

    def display_stats(self):
        shield_status = " [🛡️SHIELD ACTIVE] " if self.shield_active else ""
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Rage Stacks: {self.rage_stacks}{shield_status}")

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.mana = 100
        self.max_mana = 100
        self.mana_regen = 15 # Mana regenerated per turn

    def attack(self, opponent):
        """Mage attacks and regenerates mana."""
        opponent.health -= self.attack_power
        print(f"{self.name} casts a spell at {opponent.name} for {self.attack_power} damage!")

        # Regenerate mana
        if self.mana < self.max_mana:
            mana_gained = min(self.mana_regen, self.max_mana - self.mana)
            self.mana += mana_gained
            print(f"✨{self.name} regenerates {mana_gained} mana! Current mana: {self.mana}/{self.max_mana}")
        else:
            print(f"✨{self.name}'s mana is at maximum!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def use_special_ability(self, opponent):
        """Display special ability menu for Mage"""
        print("\n=== Mage Special Abilities ===")
        print(f"Current Mana: ✨{self.mana}/{self.max_mana}")
        print("1. Fireball - Deal massive magical damage (Costs 40 mana)")
        print("2. Ice Shield - Absorb damage and restore health (Costs 30 mana)")
        print("3. Cancel")

        choice = input("Choose an ability: ")
        if choice == '1':
            return self.fireball(opponent)
        elif choice == '2':
            return self.ice_shield()
        elif choice == '3':
            print("Cancelled special ability.")
            return False
        else:
            print("Invalid choice. Try again.")
            return self.use_special_ability(opponent)

    def fireball(self, opponent):
        """Consume mana to cast a devastating spell"""
        mana_cost = 40

        if self.mana < mana_cost:
            print(f"❌Not enough mana! Need {mana_cost}, have {self.mana}")
            print("Use regular attacks to regenerate more mana.")
            return False

        # Consume mana and deal amplified damage
        self.mana -= mana_cost
        damage = int(self.attack_power * 2)
        opponent.health -= damage

        print(f"🔥💥{self.name} casts FIREBALL!")
        print(f"A massive ball of flame engulfs {opponent.name} for {damage} damage!")
        print(f"Mana remaining: {self.mana}/{self.max_mana}")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        return True

    def ice_shield(self):
        """Consume mana to create a protective shield that heals"""
        mana_cost = 30

        if self.mana < mana_cost:
            print(f"❌Not enough mana! Need {mana_cost}, have {self.mana}")
            print("Use regular attacks to regenerate more mana.")
            return False

        # Consume mana and heal
        self.mana -= mana_cost
        heal_amount = 25
        self.health = min(self.health + heal_amount, self.max_health)

        print(f"🧊✨{self.name} conjures an ICE SHIELD!")
        print(f"Magical energy surrounds {self.name}, restoring {heal_amount} health!")
        print(f"Current health: {self.health}/{self.max_health}")
        print(f"Mana remaining: {self.mana}/{self.max_mana}")
        return True

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Mana: {self.mana}/{self.max_mana}")

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

# EvilWizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- ⚔️⚔️⚔️ Your Turn ⚔️⚔️⚔️ ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the character's special ability method
            ability_used = player.use_special_ability(wizard)
            if not ability_used:
                continue  # Let player choose again if ability wasn't used
        elif choice == '3':
            pass # Placeholder for healing
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue  # Viewing stats doesn't consume a turn
        else:
            print("Invalid choice. Try again.")
            continue

        # Wizard's turn
        if wizard.health > 0:
            print("\n--- 🧙🧙🧙 Wizard's Turn 🧙🧙🧙 ---")
            wizard.regenerate()

            # Check if player has shield active for damage calculation
            if isinstance(player, Warrior) and player.shield_active:
                actual_damage = player.take_damage(wizard.attack_power)
                print(f"{wizard.name} attacks {player.name} for {actual_damage} damage!")
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"\n💀{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"\n🎉The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    print("=" * 50)
    print("🧙 Defeat the Evil Wizard! 🧙‍")
    print("=" * 50)
    player = create_character()
    wizard = EvilWizard("Malakar the Malevolent")
    print(f"\n{player.name} faces {wizard.name}!")
    battle(player, wizard)

if __name__ == "__main__":
    main()