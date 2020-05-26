""" Start of script """
# Block list
# View the blocks in the game and their ID
# There is going to be over 10000 blocks when ready
''' Dirt ''' # Category 1
block_dirtID = int(1)
block_coarseDirtID = int(2)
block_podzolID = int(3)
block_myceliumID = int(4)
block_grassPathID = int(5)
''' Stone ''' # Category 2
block_caveStoneID = float(1.1)
block_cobbleStoneID = float(1.2)
block_mossyCobbleStoneID = float(1.3)
block_smoothStoneID = float(1.4)
block_obsidianID = float(1.5)
block_bedrockID = float(1.6)
''' Slabs ''' # Category 3
block_dirtSlabID = float(2.1)
block_coarseDirtSlabID = float(2.2)
block_podzolSlabID = float(2.3)
block_myceliumSlabID = float(2.4)
block_grassPathSlabID = float(2.5)
block_caveStoneSlabID = float(2.6)
block_mossyCobbleStoneSlabID = float(2.7)
block_smoothStoneSlabID = float(2.8)
block_obsidianSlabID = float(2.9)
block_bedrockSlabID = float(2.10)
block_gravelSlabID = float(2.11)
block_goldSlabID = float(2.12)
block_purpurSlabID = float(2.13)
block_OakWoodPlankSlabID = float(2.14)
block_darkOakWoodPlankSlabID = float(2.15)
block_acaciaWoodPlankSlabID = float(2.16)
block_birchWoodPlankSlabID = float(2.17)
block_spruceWoodPlankSlabID = float(2.18)
block_jungleWoodPlankSlabID = float(2.19)
block_cherryWoodPlankSlabID = float(2.20)
block_locustWoodPlankSlabID = float(2.21)
block_appleWoodPlankSlabID = float(2.22)
block_ashWoodPlankSlabID = float(2.23)
block_diamondSlabID = float(2.24)
block_OakWoodLogSlabID = float(2.25)
block_darkOakWoodLogSlabID = float(2.26)
block_acaciaWoodLogSlabID = float(2.27)
block_birchWoodLogSlabID = float(2.28)
block_spruceWoodLogSlabID = float(2.29)
block_jungleWoodLogSlabID = float(2.30)
block_cherryWoodLogSlabID = float(2.31)
block_locustWoodLogSlabID = float(2.32)
block_appleWoodLogSlabID = float(2.33)
block_ashWoodLogSlabID = float(2.34)
''' Stairs ''' # Category 4
block_dirtStairsID = float(3.1)
block_coarseDirtStairsID = float(3.2)
block_podzolStairsID = float(3.3)
block_obsidianStairsID = float(3.4)
block_yellowSandStairsID = float(3.5)
block_bedrockStairsID = float(3.6)
block_gravelStairsID = float(3.7)
block_myceliumStairsID = float(3.8)
block_grassPathStairsID = float(3.9)
block_mossyCobbleStoneStairsID = float(3.10)
block_cobblestoneStairsID = float(3.11)
block_smoothStoneStairsID = float(3.12)
block_goldStairsID = float(3.13)
block_purpurStairsID = float(3.14)
block_diamondStairsID = float(3.15)
''' Ores ''' # Category 5
block_coalOreID = float(4.1)
block_ironOreID = float(4.2)
block_goldOreID = float(4.3)
block_redstoneOreID = float(4.4)
block_emeraldOreID = float(4.5)
block_diamondOreID = float(4.6)
block_lapisLazuliOreID = float(4.7)
block_netherQuartzOreID = float(4.8)
block_bronzeOreID = float(4.100)
block_silverOreID = float(4.101)
block_rubyOreID = float(4.102)
''' Saplings ''' # Category 6
block_oakSaplingID = float(5.1)
block_darkOakTreeSaplingID = float(5.2)
block_acaciaTreeSaplingID = float(5.3)
block_birchTreeSaplingID = float(5.4)
block_spruceTreeSaplingID = float(5.5)
block_jungleTreeSaplingID = float(5.6)
block_cherryTreeSaplingID = float(5.7)
block_locustTreeSaplingID = float(5.8)
block_appleTreeSaplingID = float(5.9)
block_ashTreeSaplingID = float(5.10)
''' Beds ''' # Category 7
block_redBasicBedID = float(6.1)
block_blueBasicBedID = float(6.2)
block_greenBasicBedID = float(6.3)
block_cyanBasicBedID = float(6.4)
block_magentaBasicBedID = float(6.5)
block_whiteBasicBedID = float(6.6)
block_blackBasicBedID = float(6.7)
''' Wood ''' # Category 8
block_oakWoodPlankID = float(7.1)
block_darkOakWoodPlankID = float(7.2)
block_acaciaWoodPlankID = float(7.3)
block_birchWoodPlankID = float(7.4)
block_spruceWoodPlankID = float(7.5)
block_jungleWoodPlankID = float(7.6)
block_cherryWoodPlankID = float(7.7)
block_locustWoodPlankID = float(7.8)
block_appleWoodPlankID = float(7.9)
block_ashWoodPlankID = float(7.10)
block_oakWoodLogID = float(7.11)
block_darkOakWoodLogID = float(7.12)
block_acaciaWoodLogID = float(7.13)
block_birchWoodLogID = float(7.14)
block_spruceWoodLogID = float(7.15)
block_jungleWoodLogID = float(7.16)
block_cherryWoodLogID = float(7.17)
block_locustWoodLogID = float(7.18)
block_appleWoodLogID = float(7.19)
block_ashWoodLogID = float(7.20)
block_OldOakWoodLogID = float(7.21) # Old logs have rings in the middle. There can be a maximum of 8 rings. A ring automatically is created after 365 in-game days worth of time.
block_OldDarkOakWoodLogID = float(7.22)
block_OldAcaciaWoodLogID = float(7.23)
block_OldBirchWoodLogID = float(7.24)
block_OldSpruceWoodLogID = float(7.25)
block_OldJungleWoodLogID = float(7.26)
block_OldCherryWoodLogID = float(7.27)
block_OldLocustWoodLogID = float(7.28)
block_OldAppleWoodLogID = float(7.29)
block_OldAshWoodLogID = float(7.30)
''' Nether ''' # Category 9
block_magmaBlockID = float(8.1)
block_netherrackID = float(8.2)
block_soulSandID = float(8.3)
block_glowStoneID = float(8.4)
block_netherBrickBlockID = float(8.5)
block_redNetherBrickBlockID = float(8.6)
''' Glass ''' # Category 10
block_glassID = float(9.1)
block_glassPaneID = float(9.2)
block_whiteStainedGlassID = float(9.3)
block_whiteStainedGlassPaneID = float(9.4)
''' Appliances ''' # Category 11
block_furnaceID = float(10.1)
block_enderChestID = float(10.2)
block_OakWoodCraftingTableID = float(10.3)
block_ironCauldronID = float(10.4)
block_ironSpawnerCageID = float(10.5)
block_jukeBoxID = float(10.6)
block_oakWoodNoteblockID = float(10.7)
block_darkOakWoodNoteblockID = float(10.8)
block_acaciaWoodNoteblockID = float(10.9)
block_birchWoodNoteBlockID = float(10.10)
block_spruceWoodNoteBlockID = float(10.11)
block_jungleWoodNoteBlockID = float(10.12)
block_cherryWoodNoteBlockID = float(10.13)
block_locustWoodNoteBlockID = float(10.14)
block_appleWoodNoteBlockID = float(10.15)
block_ashWoodNoteBlockID = float(10.16)
block_DarkOakWoodCraftingTableID = float(10.17)
block_acaciaWoodCraftingTableID = float(10.18)
block_birchWoodCraftingTableID = float(10.19)
block_spruceWoodCraftingTableID = float(10.20)
block_jungleWoodCraftingTableID = float(10.21)
block_cherryWoodCraftingTableID = float(10.22)
block_locustWoodCraftingTableID = float(10.23)
block_appleWoodCraftingTableID = float(10.24)
block_ashWoodCraftingTableID = float(10.25)
block_chestID = float(10.26)
block_barrelID = float(10.27)
block_ironAnvilID = float(10.28)
block_slightlyDamagedIronAnvilID = float(10.29)
block_heavilyDamagedIronAnvilID = float(10.30)
block_steelAnvilID = float(10.31)
block_slightlyDamagedsteelAnvilID = float(10.32)
block_heavilyDamagedsteelAnvilID = float(10.33)
block_diamondAnvilID = float(10.34)
block_slightlyDamagedDiamondAnvilID = float(10.35)
block_heavilyDamagedDiamondAnvilID = float(10.36)
block_blastFurnaceID = float(10.37)
block_enderDispenserID = float(10.38)
block_dispenserID = float(10.39)
block_bookshelfID = float(10.40)
block_lecternID = float(10.41)
block_loomID = float(10.42)
block_netherReactorCoreID = float(10.43)
block_airConditionerBlockID = float(10.44)
''' Doors ''' # Category 12
block_ironDoorID = float(11.1)
block_steelDoorID = float(11.2)
block_oakWoodDoorID = float(11.3)
block_darkOakWoodDoorID = float(11.4)
block_acaciaWoodDoorID = float(11.5)
block_birchWoodDoorID = float(11.6)
block_spruceWoodDoorID = float(11.7)
block_jungleWoodDoorID = float(11.8)
block_cherryWoodDoorID = float(11.9)
block_locustWoodDoorID = float(11.10)
block_appleWoodDoorID = float(11.11)
block_ashWoodDoorID = float(11.12)
block_obsidianDoorID = float(11.13)
block_caveStoneDoorID = float(11.14)
block_goldDoorID = float(11.15)
block_diamondDoorID = float(11.16)
block_aluminumDoorID = float(11.17)
block_tinDoorID = float(11.18)
block_diamondDoorID = float(11.19)
block_emeraldDoorID = float(11.20)
block_ironTrapDoorID = float(11.21)
block_steeTraplDoorID = float(11.22)
block_oakWoodTrapDoorID = float(11.23)
block_darkOakWoodTrapDoorID = float(11.24)
block_acaciaWoodTrapDoorID = float(11.25)
block_birchWoodTrapDoorID = float(11.26)
block_spruceWoodTrapDoorID = float(11.27)
block_jungleWoodTrapDoorID = float(11.28)
block_cherryWoodTrapDoorID = float(11.29)
block_locustWoodTrapDoorID = float(11.30)
block_appleWoodTrapDoorID = float(11.31)
block_ashWoodTrapDoorID = float(11.32)
block_obsidianTrapDoorID = float(11.33)
block_caveStoneTrapDoorID = float(11.34)
block_goldTrapDoorID = float(11.35)
block_diamondTrapDoorID = float(11.36)
block_aluminumTrapDoorID = float(11.37)
block_tinTrapDoorID = float(11.38)
block_diamondTrapDoorID = float(11.39)
block_emeraldTrapDoorID = float(11.40)
''' End ''' # Category 13
block_purpleEndCrystalID = float(12.1)
block_endStoneID = float(12.2)
block_enderDragonEggID = float(12.3)
block_endPortalID = float(12.4)
block_purpurBlockID = float(12.5)
block_purpurPillarBlockID = float(12.6)
''' Clay ''' # Category 14
block_clayID = float(13.1)
block_whiteClayID = float(13.2)
block_blackClayID = float(13.3)
block_limeClayID = float(13.4)
block_greenClayID = float(13.5)
block_cyanClayID = float(13.6)
block_turquioseClayID = float(13.7)
block_yellowClayID = float(13.8)
block_lightBlueClayID = float(13.9)
block_darkBlueClayID = float(13.10)
block_lightGreyClayID = float(13.11)
block_darkGreyClayID = float(13.12)
block_redClayID = float(13.13)
block_pinkClayID = float(13.14)
block_purpleClayID = float(13.15)
block_brownClayID = float(13.16)
block_orangeClayID = float(13.17)
block_hardenedwhiteClayID = float(13.18)
block_hardenedblackClayID = float(13.19)
block_hardenedlimeClayID = float(13.20)
block_hardenedgreenClayID = float(13.21)
block_hardenedcyanClayID = float(13.22)
block_hardenedturquioseClayID = float(13.23)
block_hardenedyellowClayID = float(13.24)
block_hardenedlightBlueClayID = float(13.25)
block_hardeneddarkBlueClayID = float(13.26)
block_hardenedlightGreyClayID = float(13.27)
block_hardeneddarkGreyClayID = float(13.28)
block_hardenedredClayID = float(13.29)
block_hardenedpinkClayID = float(13.30)
block_hardenedpurpleClayID = float(13.31)
block_hardenedbrownClayID = float(13.32)
block_hardenedorangeClayID = float(13.33)
''' Terracotta ''' # Category 15
block_whiteArrowTerracottaID = float(14.1)
''' Concrete ''' # Category 16
block_whiteConcretePowderID = float(15.1)
block_whiteConcreteID = float(15.2)
block_blackConcretePowderID = float(15.3)
block_blackConcreteID = float(15.4)
block_lightGreyConcretePowderID = float(15.5)
block_lightGreyConcreteID = float(15.6)
block_darkGreyConcretePowderID = float(15.7)
block_darkGreyConcreteID = float(15.8)
''' Carpet ''' # Category 17
block_whiteCarpetID = float(16.1)
''' Wool ''' # Category 18
block_whiteWoolID = float(17.1)
''' Redstone ''' # Category 19
block_redstoneBlockID = float(18.1)
block_redstoneTorchID = float(18.2)
block_goldenPressurePlateID = float(18.3)
block_CaveStoneLeverID = float(18.4)
block_cobbleStoneButtonID = float(18.5)
block_caveStoneButtonID = float(18.6)
block_pistonID = float(18.7)
block_stickyPistonID = float(18.8)
block_oakWoodPressurePlateID = float(18.9)
block_darkOakWoodPressurePlateID = float(18.10)
block_acaciaWoodPressurePlateID = float(18.11)
block_birchWoodPressurePlateID = float(18.12)
block_spruceWoodPressurePlateID = float(18.13)
block_jungleWoodPressurePlateID = float(18.14)
block_cherryWoodPressurePlateID = float(18.15)
block_locustWoodPressurePlateID = float(18.16)
block_appleWoodPressurePlateID = float(18.17)
block_ashWoodPressurePlateID = float(18.18)
block_pythonCommandBlockID = float(18.19)
block_NormalcommandBlockID = float(18.20)
block_redstoneRepeaterID = float(18.21)
block_redstoneComparterID = float(18.22)
block_daylightSensorID = float(18.23)
block_hopperID = float(18.24)
block_dropperID = float(18.25)
block_ironCashRegisterID = float(18.26)
block_redstoneLampBlockID = float(18.27)
block_redstoneID = float(18.28)
''' On the wall ''' # Category 20
block_painting1ID = float(19.1)
block_torchID = float(19.2)
block_steveHeadID = float(19.3)
block_alexHeadID = float(19.4)
block_herobrineHeadID = float(19.5)
block_notchHeadID = float(19.6)
block_skeletonSkullID = float(19.7)
block_witherSkeletonSkullID = float(19.8)
block_creeperHeadID = float(19.9)
block_enderDragonHeadID = float(19.10)
block_endermanHeadID = float(19.11)
block_zombieHeadID = float(19.12)
block_villagerZombieHeadID = float(19.13)
block_chickenHeadID = float(19.14)
block_pigHeadID = float(19.15)
block_villagerHeadID = float(19.16)
''' Frozen ''' # Category 21
block_snowBlockID = float(20.1)
block_snowID = float(20.2)
block_iceBlockID = float(20.3)
block_packedIceBlockID = float(20.4)
block_blueIceBlockID = float(20.5)
block_greenIceBlockID = float(20.6)
''' Fence-like ''' # Category 22
block_ironBarsID = float(21.1)
block_steelBarsID = float(21.2)
block_diamondBarsID = float(21.3)
block_oakWoodFenceID = float(21.4)
block_oakWoodWallID = float(21.5)
block_darkOakWoodFenceID = float(21.6)
block_darkOakWoodWallID = float(21.7)
block_acaciaWoodFenceID = float(21.8)
block_acaciaWoodWallID = float(21.9)
block_birchWoodFenceID = float(21.10)
block_spruceWoodFenceID = float(21.11)
block_jungleWoodFenceID = float(21.12)
block_cherryWoodFenceID = float(21.13)
block_locustWoodFenceID = float(21.14)
block_appleWoodFenceID = float(21.15)
block_ashWoodFenceID = float(21.16)
block_birchWoodWallID = float(21.17)
block_spruceWoodWallID = float(21.18)
block_jungleWoodWallID = float(21.19)
block_cherryWoodWallID = float(21.20)
block_locustWoodWallID = float(21.21)
block_appleWoodWallID = float(21.22)
block_ashWoodWallID = float(21.23)
''' Ocean Monument ''' # Category 23
block_prismarineBlockID = float(22.1)
block_prismarineBrickBlockID = float(22.2)
block_seaLanternBlockID = float(22.3)
''' Solid Ores ''' # Category 24
block_steelBlockID = float(23.1)
block_diamondBlockID = float(23.2)
block_ironBlockID = float(23.3)
block_goldBlockID = float(23.4)
block_emeraldBlockID = float(23.5)
block_BronzeBlockID = float(23.6)
block_silverBlockID = float(23.7)
block_rubyBlockID = float(23.8)
block_lapisLazuliBlockID = float(23.9)
block_coalBlockID = float(23.10)
block_aluminumOreBlockID = float(23.11)
block_tinOreBlockID = float(23.12)
''' Liquid ''' # Category 25
block_waterBlockID = float(24.1)
block_coldWaterBlockID = float(24.2)
block_soulWaterBlockID = float(24.3)
block_magmaWaterBlockID = float(24.4)
block_redLavaBlockID = float(24.5)
block_orangeLavaBlockID = float(24.6)
block_plainMilkBlockID = float(24.7)
block_chocolateMilkBlockID = float(24.8)
block_strawberryMilkBlockID = float(24.9)
block_greenAciBlockID = float(24.10)
block_urineBlockID = float(24.11)
block_oilBlockID = float(24.12)
block_tarBlockID = float(24.13)
block_gasolineBlockID = float(24.14)
block_petroleumBlockID = float(24.15)
block_steamingWaterBlockID = float(24.16)
block_javaID = float(24.17)
''' Bones ''' # Category 26
block_ribcageBlockID = float(25.1)
block_skullBlockID = float(25.2)
''' Helpful ''' # Category 27
block_spongeID = float(26.1)
block_wetSpongeID = float(26.2)
''' Transportation ''' # Category 28
block_poweredRailID = float(27.1)
block_normalRailID = float(27.2)
block_activatorRailID = float(27.3)
block_wallRailID = float(27.4)
block_ceilingRailID = float(27.5)
block_oakWoodLadderID = float(27.6)
block_darkOakWoodLadderID = float(27.7)
block_acaciaWoodLadderID = float(27.8)
block_birchWoodLadderID = float(27.9)
block_spruceWoodLadderID = float(27.10)
block_JungleWoodLadderID = float(27.11)
block_cherryWoodLadderID = float(27.12)
block_locustWoodLadderID = float(27.13)
block_appleWoodLadderID = float(27.14)
block_ashWoodLadderID = float(27.15)
block_vineID = float(27.16)
block_policeCarID = float(27.17)
block_firetruckID = float(27.18)
block_ambulanceID = float(27.19)
block_steelRowingBoatID = float(27.20)
block_diamondRowingBoatID = float(27.21)
block_oakWoodRowingBoatID = float(27.22)
block_darkOakWoodRowingBoatID = float(27.23) 
block_acaciaWoodRowingBoatID = float(27.24)
block_birchWoodRowingBoatID = float(27.25)
block_spruceWoodRowingBoatID = float(27.26)
block_jungleWoodRowingBoatID = float(27.27)
block_cherryWoodRowingBoatID = float(27.28)
block_locustWoodRowingBoatID = float(27.29)
block_appleWoodRowingBoatID = float(27.30)
block_ashWoodRowingBoatID = float(27.31)
block_aluminumRowingBoatID = float(27.32)
block_ironRowingBoatID = float(27.33)
block_obsidianRowingBoatID = float(27.34)
block_tinRowingBoatID = float(27.35)
block_goldRowingBoatID = float(27.36)
block_emeraldRowingBoatID = float(27.37)
block_diamondRowingBoatID = float(27.38)
block_ironMinecartID = float(27.39)
block_ironMinecartWithEnderChestID = float(27.40)
block_ironMinecartWithChestID = float(27.41)
block_ironMinecartWithTNTID = float(27.42)
block_ironMinecartWithDynamiteID = float(27.43)
block_ironMinecartWithFurnaceID = float(27.44)
block_ironMinecartWithBlastFurnaceID = float(27.45)
block_ironMinecartWithHopperID = float(27.46)
''' Desert caves ''' # Category 29
block_yellowSandBlockID = float(28.1)
block_redSandBlockID = float(28.2)
block_blueSandBlockID = float(28.3)
block_greenSandBlockID = float(28.4)
block_blackSandBlockID = float(28.4)
block_orangeSandBlockID = float(28.6)
block_yellowSandStoneBlockID = float(28.7)
block_smoothYellowSandStoneBlockID = float(28.8)
block_carvedYellowSandStoneBlockID = float(28.9)
block_redSandStoneBlockID = float(28.10)
block_smoothRedSandStoneBlockID = float(28.11)
block_carvedRedSandStoneBlockID = float(28.12)
block_blueSandStoneBlockID = float(28.13)
block_smoothBlueSandStoneBlockID = float(28.14)
block_carvedBlueSandStoneBlockID = float(28.15)
block_greenSandStoneBlockID = float(28.16)
block_smoothGreenSandStoneBlockID = float(28.17)
block_carvedGreenSandStoneBlockID = float(28.18)
block_blackSandStoneBlockID = float(28.19)
block_smoothBlackSandStoneBlockID = float(28.20)
block_carvedBlackSandStoneBlockID = float(28.21)
block_orangeSandStoneBlockID = float(28.22)
block_smoothOrangeSandStoneBlockID = float(28.23)
block_carvedOrangeSandStoneBlockID = float(28.24)
block_gravelBlockID = float(28.25)
block_cactusID = float(28.26)
block_cobwebID = float(28.27)
''' Classic explosives ''' # Category 30
block_TNTBlockID = float(29.1)
block_dynamiteBlockID = float(29.2)
''' Quartz and urban blocks ''' # Category 31
block_quartzBlockID = float(30.1)
block_beaconID = float(30.2)
block_quartzPillarBlockID = float(30.3)
block_smoothQuartzBlockID = float(30.4)
block_chiseledQuartzBlockID = float(30.5)
''' Other1s ''' # Category xx
block_hayBaleBlockID = float(100.1)
block_slimeBlockID = float(100.2)
''' Move '''
# Section "items" moved to separate file on 7.22.2019
# Section "mobs" moved to separate file on 7.22.2019
''' ToDo '''
# make slabs and stairs of every block type
# Separate the files
# Get all 10 wood types of most items written in
""" End of script """
