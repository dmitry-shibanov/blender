#pragma once

#include "FN_core.hpp"
#include "lists.hpp"
#include "numeric.hpp"

namespace FN {
namespace Types {

using SharedFloatList = SharedList<float>;
using SharedFloat3List = SharedList<float3>;
using SharedInt32List = SharedList<int32_t>;
using SharedBoolList = SharedList<bool>;

SharedType &GET_TYPE_float_list();
SharedType &GET_TYPE_float3_list();
SharedType &GET_TYPE_int32_list();
SharedType &GET_TYPE_bool_list();

}  // namespace Types
}  // namespace FN
