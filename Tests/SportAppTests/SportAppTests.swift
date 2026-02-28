import Testing
@testable import SportApp

@Test func fixturesLoadSuccessfully() {
    let fixtures = FixtureLoader.loadFixtures()

    #expect(fixtures.count == 3)
    #expect(fixtures.first?.homeTeam == "Galatasaray")
    #expect(fixtures.last?.league == "EuroLeague")
}
