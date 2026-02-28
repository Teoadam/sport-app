import Foundation

struct Match: Codable {
    let homeTeam: String
    let awayTeam: String
    let date: String
    let league: String

    var formatted: String {
        "\(date) | \(league): \(homeTeam) vs \(awayTeam)"
    }
}

enum FixtureLoader {
    static func loadFixtures() -> [Match] {
        let json = """
        [
          {"homeTeam":"Galatasaray","awayTeam":"Fenerbahçe","date":"2026-03-10","league":"Süper Lig"},
          {"homeTeam":"Beşiktaş","awayTeam":"Trabzonspor","date":"2026-03-12","league":"Süper Lig"},
          {"homeTeam":"Anadolu Efes","awayTeam":"Fenerbahçe Beko","date":"2026-03-18","league":"EuroLeague"}
        ]
        """

        let data = Data(json.utf8)
        let decoder = JSONDecoder()

        return (try? decoder.decode([Match].self, from: data)) ?? []
    }
}

@main
struct SportApp {
    static func main() {
        print("🏟️ SportApp - Yaklaşan Maçlar")
        print(String(repeating: "-", count: 34))

        let fixtures = FixtureLoader.loadFixtures()

        guard !fixtures.isEmpty else {
            print("Maç verisi bulunamadı.")
            return
        }

        fixtures.forEach { print($0.formatted) }
    }
}
