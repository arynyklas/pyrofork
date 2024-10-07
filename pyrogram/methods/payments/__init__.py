#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from .apply_gift_code import ApplyGiftCode
from .check_giftcode import CheckGiftCode
from .create_invoice_link import CreateInvoiceLink
from .get_payment_form import GetPaymentForm
from .get_star_gifts import GetStarGifts
from .get_stars_transactions import GetStarsTransactions
from .get_stars_transactions_by_id import GetStarsTransactionsById
from .refund_stars_payment import RefundStarPayment
from .send_invoice import SendInvoice
from .send_paid_media import SendPaidMedia
from .send_paid_reaction import SendPaidReaction
from .send_payment_form import SendPaymentForm

class Payments(
    ApplyGiftCode,
    CheckGiftCode,
    CreateInvoiceLink,
    GetPaymentForm,
    GetStarGifts,
    GetStarsTransactions,
    GetStarsTransactionsById,
    RefundStarPayment,
    SendPaidReaction,
    SendPaidMedia,
    SendInvoice,
    SendPaymentForm
):
    pass
