#include <algorithm>
#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <string>
#include <vector>

static std::string _dq(const unsigned char* _p, size_t _n) {
    std::string _r;
    _r.reserve(_n);
    for (size_t _i = 0; _i < _n; ++_i) _r.push_back(static_cast<char>(_p[_i] ^ 0x5A));
    return _r;
}

static const unsigned char _k00[] = {31,52,46,63,40,122,46,50,63,122,62,51,40,63,57,46,53,40,35,122,42,59,46,50,122,57,53,52,46,59,51,52,51,52,61,122,116,34,57,60,122,60,51,54,63,41,96,122};
#define _K00 _dq(_k00, sizeof(_k00))
static const unsigned char _k01[] = {31,40,40,53,40,96,122,25,53,47,54,62,122,52,53,46,122,40,63,59,62,122,62,51,40,63,57,46,53,40,35,116};
#define _K01 _dq(_k01, sizeof(_k01))
static const unsigned char _k02[] = {116,2,25,28};
#define _K02 _dq(_k02, sizeof(_k02))
static const unsigned char _k03[] = {31,40,40,53,40,96,122,25,53,47,54,62,122,52,53,46,122,62,63,54,63,46,63,122,60,51,54,63,122};
#define _K03 _dq(_k03, sizeof(_k03))
static const unsigned char _k04[] = {96,122};
#define _K04 _dq(_k04, sizeof(_k04))
static const unsigned char _k05[] = {30,63,54,63,46,63,62,122,60,51,54,63,96,122};
#define _K05 _dq(_k05, sizeof(_k05))
static const unsigned char _k06[] = {31,40,40,53,40,96,122,30,51,40,63,57,46,53,40,35,122,42,59,46,50,122,57,59,52,52,53,46,122,56,63,122,63,55,42,46,35,116};
#define _K06 _dq(_k06, sizeof(_k06))
static const unsigned char _k07[] = {31,40,40,53,40,96,122,30,51,40,63,57,46,53,40,35,122,62,53,63,41,122,52,53,46,122,63,34,51,41,46,122,53,40,122,51,41,122,52,53,46,122,59,122,62,51,40,63,57,46,53,40,35,116};
#define _K07 _dq(_k07, sizeof(_k07))
static const unsigned char _k08[] = {20,53,122,116,34,57,60,122,60,51,54,63,41,122,60,53,47,52,62,122,51,52,122,46,50,63,122,62,51,40,63,57,46,53,40,35,116};
#define _K08 _dq(_k08, sizeof(_k08))

std::string _f0() {
    std::string _v0;
    std::cout << _K00;
    std::getline(std::cin, _v0);
    return _v0;
}

bool _f1(const std::string& _v0) {
    std::filesystem::path _v1(_v0);
    std::error_code _v2;
    return std::filesystem::exists(_v1, _v2) && std::filesystem::is_directory(_v1, _v2);
}

std::vector<std::filesystem::path> _f2(const std::string& _v0) {
    std::vector<std::filesystem::path> _v5;
    std::filesystem::path _v1(_v0);
    std::error_code _v2;
    for (const auto& _v3 : std::filesystem::directory_iterator(_v1, _v2)) {
        if (_v2) {
            std::cerr << _K01 << std::endl;
            return {};
        }
        if (_v3.is_regular_file(_v2) && !_v2) {
            std::string _v4 = _v3.path().extension().string();
            std::transform(_v4.begin(), _v4.end(), _v4.begin(), [](unsigned char _c) {
                return static_cast<char>(std::toupper(_c));
            });
            if (_v4 == _K02) {
                _v5.push_back(_v3.path());
            }
        }
    }
    return _v5;
}

void _f3(const std::vector<std::filesystem::path>& _v5) {
    for (const auto& _v6 : _v5) {
        std::error_code _v2;
        std::filesystem::remove(_v6, _v2);
        if (_v2) {
            std::cerr << _K03 << _v6 << _K04 << _v2.message() << std::endl;
        } else {
            std::cout << _K05 << _v6 << std::endl;
        }
    }
}

int main() {
    std::string _v0 = _f0();
    if (_v0.empty()) {
        std::cerr << _K06 << std::endl;
        return 1;
    }
    if (!_f1(_v0)) {
        std::cerr << _K07 << std::endl;
        return 1;
    }
    std::vector<std::filesystem::path> _v5 = _f2(_v0);
    if (_v5.empty()) {
        std::cout << _K08 << std::endl;
        return 0;
    }
    _f3(_v5);
    return 0;
}
