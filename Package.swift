// swift-tools-version: 6.1
import PackageDescription

let package = Package(
    name: "SportApp",
    platforms: [
        .macOS(.v13)
    ],
    products: [
        .executable(name: "SportApp", targets: ["SportApp"])
    ],
    targets: [
        .executableTarget(
            name: "SportApp"
        ),
        .testTarget(
            name: "SportAppTests",
            dependencies: ["SportApp"]
        )
    ]
)
